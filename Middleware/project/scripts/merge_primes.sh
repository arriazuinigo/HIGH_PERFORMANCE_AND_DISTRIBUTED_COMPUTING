#!/bin/bash
# SLURM merge job: deduplicates and sorts all partial result files into
# results/ALL_PRIMES.txt.  Submitted by the orchestrator with
# --dependency=afterok:<array_job_id> so it only runs when every array task
# has completed successfully.
#
#SBATCH --job-name=merge_primes
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:10:00

# Arguments passed by the orchestrator:
#   $1 = path to results/
#   $2 = path to scripts/

RESULTS_DIR="$1"
SCRIPTS_DIR="$2"

if [[ -z "$RESULTS_DIR" || -z "$SCRIPTS_DIR" ]]; then
    echo "Usage: $0 <results_dir> <scripts_dir>" >&2
    exit 1
fi

echo "Merging prime results from: ${RESULTS_DIR}"

/soft/Miniconda3/bin/python "${SCRIPTS_DIR}/merge_primes.py" "$RESULTS_DIR"
