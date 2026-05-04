#!/usr/bin/env python3
"""
Workflow orchestrator for distributed prime-number computation.

Scans data/ for sample folders, collects all (start, end) ranges from
ranges_*.txt files, and submits a SLURM job array so each range is computed
in parallel on the cluster. A dependent merge job then deduplicates and sorts
all results into results/ALL_PRIMES.txt.

Usage
-----
    python workflow_orchestrator.py                    # run from project dir
    python workflow_orchestrator.py /path/to/project   # run from anywhere
"""

import os
import sys
import subprocess
import datetime
import glob


# ---------------------------------------------------------------------------
# Logging helper
# ---------------------------------------------------------------------------

def log(logfile: str, msg: str) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    with open(logfile, "a") as fh:
        fh.write(line + "\n")


# ---------------------------------------------------------------------------
# Main orchestration logic
# ---------------------------------------------------------------------------

def main() -> None:
    # ------------------------------------------------------------------ #
    # 0. Resolve project directory and sub-paths                          #
    # ------------------------------------------------------------------ #
    project_dir = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()

    data_dir    = os.path.join(project_dir, "data")
    results_dir = os.path.join(project_dir, "results")
    logs_dir    = os.path.join(project_dir, "logs")
    scripts_dir = os.path.join(project_dir, "scripts")

    os.makedirs(results_dir, exist_ok=True)
    os.makedirs(logs_dir,    exist_ok=True)

    logfile = os.path.join(logs_dir, "ORCHEST_LOG.txt")
    log(logfile, "=" * 60)
    log(logfile, f"Orchestrator started.")
    log(logfile, f"  Project dir : {project_dir}")
    log(logfile, f"  Data dir    : {data_dir}")
    log(logfile, f"  Results dir : {results_dir}")
    log(logfile, f"  Logs dir    : {logs_dir}")
    log(logfile, f"  Scripts dir : {scripts_dir}")

    # ------------------------------------------------------------------ #
    # 1. Collect tasks: (start, end, output_path) for every range line    #
    # ------------------------------------------------------------------ #
    if not os.path.isdir(data_dir):
        log(logfile, f"ERROR: data directory not found: {data_dir}")
        sys.exit(1)

    sample_dirs = sorted(
        d for d in glob.glob(os.path.join(data_dir, "sample_*"))
        if os.path.isdir(d)
    )

    if not sample_dirs:
        log(logfile, "ERROR: no sample_* folders found inside data/.")
        sys.exit(1)

    log(logfile, f"Found {len(sample_dirs)} sample folder(s).")

    tasks = []  # list of (start: str, end: str, output_path: str)

    for sample_dir in sample_dirs:
        sample_name  = os.path.basename(sample_dir)
        log(logfile, f"  Visiting sample folder: {sample_name}")

        ranges_files = sorted(glob.glob(os.path.join(sample_dir, "ranges_*.txt")))
        log(logfile, f"    Found {len(ranges_files)} ranges file(s).")

        for ranges_file in ranges_files:
            ranges_basename = os.path.basename(ranges_file)
            log(logfile, f"    Processing: {ranges_basename}")

            with open(ranges_file, "r") as fh:
                lines = [l.strip() for l in fh if l.strip()]

            for line_num, line in enumerate(lines, start=1):
                parts = line.split()
                if len(parts) != 2:
                    log(logfile, f"      WARNING: skipping malformed line {line_num}: '{line}'")
                    continue

                start, end = parts[0], parts[1]
                ranges_stem = os.path.splitext(ranges_basename)[0]
                out_name    = f"{sample_name}_{ranges_stem}_line{line_num}.txt"
                out_path    = os.path.join(results_dir, out_name)

                tasks.append((start, end, out_path))
                log(logfile, f"      Task {len(tasks):4d}: [{start:>10}, {end:>10}] -> {out_name}")

    if not tasks:
        log(logfile, "ERROR: No valid range lines found. Check data/ contents.")
        sys.exit(1)

    log(logfile, f"Total tasks collected: {len(tasks)}")

    # ------------------------------------------------------------------ #
    # 2. Write tasks index file (line N = SLURM array task N)             #
    # ------------------------------------------------------------------ #
    tasks_file = os.path.join(scripts_dir, "tasks.txt")
    with open(tasks_file, "w") as fh:
        for start, end, out_path in tasks:
            fh.write(f"{start} {end} {out_path}\n")

    log(logfile, f"Tasks index file written: {tasks_file}  ({len(tasks)} entries)")

    # ------------------------------------------------------------------ #
    # 3. Submit SLURM array job – one task per range line                 #
    # ------------------------------------------------------------------ #
    array_script = os.path.join(scripts_dir, "run_primes_array.sh")
    n_tasks      = len(tasks)

    sbatch_array_cmd = [
        "sbatch",
        f"--array=1-{n_tasks}",
        f"--output={os.path.join(logs_dir, 'primes_%A_%a.out')}",
        f"--error={os.path.join(logs_dir,  'primes_%A_%a.err')}",
        array_script,
        tasks_file,
        scripts_dir,
    ]

    log(logfile, f"Submitting SLURM array job ({n_tasks} tasks):")
    log(logfile, "  " + " ".join(sbatch_array_cmd))

    result = subprocess.run(sbatch_array_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        log(logfile, f"ERROR: sbatch failed (array job):\n{result.stderr.strip()}")
        sys.exit(1)

    # sbatch prints: "Submitted batch job <id>"
    array_job_id = result.stdout.strip().split()[-1]
    log(logfile, f"SLURM array job submitted: job_id={array_job_id}  (tasks 1-{n_tasks})")

    # ------------------------------------------------------------------ #
    # 4. Submit merge job – depends on all array tasks completing OK      #
    # ------------------------------------------------------------------ #
    merge_script = os.path.join(scripts_dir, "merge_primes.sh")

    sbatch_merge_cmd = [
        "sbatch",
        f"--dependency=afterok:{array_job_id}",
        f"--output={os.path.join(logs_dir, 'merge_%j.out')}",
        f"--error={os.path.join(logs_dir,  'merge_%j.err')}",
        merge_script,
        results_dir,
        scripts_dir,
    ]

    log(logfile, f"Submitting SLURM merge job (depends on afterok:{array_job_id}):")
    log(logfile, "  " + " ".join(sbatch_merge_cmd))

    result2 = subprocess.run(sbatch_merge_cmd, capture_output=True, text=True)
    if result2.returncode != 0:
        log(logfile, f"ERROR: sbatch failed (merge job):\n{result2.stderr.strip()}")
        sys.exit(1)

    merge_job_id = result2.stdout.strip().split()[-1]
    log(logfile, f"SLURM merge job submitted: job_id={merge_job_id}  "
                 f"(depends on afterok:{array_job_id})")

    # ------------------------------------------------------------------ #
    # 5. Summary                                                          #
    # ------------------------------------------------------------------ #
    log(logfile, "-" * 60)
    log(logfile, "All SLURM jobs submitted successfully.")
    log(logfile, f"  Array job ID  : {array_job_id}  ({n_tasks} parallel tasks)")
    log(logfile, f"  Merge job ID  : {merge_job_id}  (runs after all array tasks)")
    log(logfile, f"  Final output  : {os.path.join(results_dir, 'ALL_PRIMES.txt')}")
    log(logfile, f"  SLURM logs in : {logs_dir}/")
    log(logfile, "Orchestrator finished.")
    log(logfile, "=" * 60)


if __name__ == "__main__":
    main()
