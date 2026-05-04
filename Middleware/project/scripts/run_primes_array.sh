#!/bin/bash
# SLURM array job: each task computes primes for one (start, end) range.
#
# --array, --output, --error are supplied by the orchestrator at submission
# time; the values below are fallback defaults only.
#
#SBATCH --job-name=count_primes
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:30:00

# Arguments passed by the orchestrator:
#   $1 = path to tasks.txt  (one "start end output_path" per line, 1-indexed)
#   $2 = path to scripts/   (directory containing count_tot_primes.py)

TASKS_FILE="$1"
SCRIPTS_DIR="$2"

if [[ -z "$TASKS_FILE" || -z "$SCRIPTS_DIR" ]]; then
    echo "Usage: $0 <tasks_file> <scripts_dir>" >&2
    exit 1
fi

# Read the line that corresponds to this array task (SLURM_ARRAY_TASK_ID is 1-based)
LINE=$(sed -n "${SLURM_ARRAY_TASK_ID}p" "$TASKS_FILE")

START=$(echo "$LINE" | awk '{print $1}')
END=$(echo "$LINE"   | awk '{print $2}')
OUT=$(echo "$LINE"   | awk '{print $3}')

if [[ -z "$START" || -z "$END" || -z "$OUT" ]]; then
    echo "ERROR: could not parse task line ${SLURM_ARRAY_TASK_ID}: '${LINE}'" >&2
    exit 1
fi

echo "Array task ${SLURM_ARRAY_TASK_ID}: primes in [${START}, ${END}] -> ${OUT}"

/soft/Miniconda3/bin/python "${SCRIPTS_DIR}/count_tot_primes.py" "$START" "$END" > "$OUT"
