# High Performance & Distributed Computing — Session 7: SLURM (1)

**Date:** 2026-03-03 (Tue)
**Instructor:** Miquel Àngel Senar Rosell (UAB)

---

## 1. Overview

This session introduces **SLURM** (Simple Linux Utility for Resource Management), a workload manager for HPC clusters. SLURM manages job scheduling across multiple machines, enabling parallel execution beyond a single node.

---

## 2. Key Concepts

### 2.1 Why SLURM?

- Previous tools (`xargs`, `parallel`) work on a **single machine**
- Clusters have **multiple nodes**, each with multiple cores
- SLURM manages resource allocation across the entire cluster
- Users submit jobs; SLURM schedules them on available resources

### 2.2 Basic SLURM Commands

| Command | Purpose |
|---------|---------|
| `sinfo` | Display node and partition information |
| `squeue` | Show job queue (waiting/running jobs) |
| `sbatch` | Submit a batch job (non-interactive) |
| `srun` | Run a job interactively or within a batch script |
| `scancel` | Cancel a job |
| `sacct` | Display accounting/history of jobs |

### 2.3 Job Submission with `sbatch`

- Create a **bash script** with SLURM directives (`#SBATCH`)
- Submit with: `sbatch script.sh`
- SLURM allocates resources and executes when available

**Basic directives:**
```bash
#!/bin/bash
#SBATCH --job-name=MyJob
#SBATCH --output=output.txt
#SBATCH --error=error.txt
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
```

### 2.4 Interactive Jobs with `srun`

- `srun` can run commands directly on allocated nodes
- Useful for testing before submitting batch jobs
- Can be used inside sbatch scripts to launch parallel tasks

### 2.5 Parametric Jobs

Three mechanisms for parameterization:

| Mechanism | Description | Where usable |
|-----------|-------------|-------------|
| **Script arguments** | `$1`, `$2`, etc. from command line | Body of script (standard bash) |
| **Environment variables** | `$SLURM_JOB_ID`, `$SLURM_JOB_NAME`, etc. | Body of script |
| **Replacement symbols** | `%j`, `%x`, etc. | Only in `#SBATCH` directives (header) |

**Common environment variables:**
- `$SLURM_JOB_ID` — unique job identifier
- `$SLURM_JOB_NAME` — name of the job
- `$SLURM_NTASKS` — number of tasks requested
- `$SLURM_NNODES` — number of nodes allocated

**Common replacement symbols:**
- `%j` — Job ID
- `%x` — Job name

### 2.6 Q&A Highlights

**Question (Szymon Majorek):** How to run multiple processes inside a single job?

**Answer:**
- Request more cores via `--ntasks` or `--cpus-per-task`
- Use `&` (ampersand) inside the script to launch multiple background processes
- Use `srun` to launch tasks across allocated resources
- Cluster nodes typically have 12 cores each — that's the maximum per node

---

## 3. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. Recap** | 0:05–1:14 | Review of single-machine parallel tools |
| **II. SLURM Introduction** | 1:14–1:15 | Why SLURM, cluster architecture |
| **III. Parametric Jobs** | 1:15:38–1:21 | Script arguments, env variables, replacement symbols |
| **IV. Q&A** | 1:21–1:24 | Multiple processes in one job |
| **V. Exercises** | 1:24–1:26 | Practice assignments |

---

## 4. Homework / Exercises

1. Submit a simple batch job using `sbatch`
2. Run a Python application through SLURM
3. Create a **parametric SLURM job** using script arguments, environment variables, or replacement symbols
4. Practice with `sinfo`, `squeue`, and `scancel`

---

## 5. Key Takeaways

- **SLURM** manages resources across multiple nodes in a cluster
- `sbatch` for batch submission; `srun` for interactive/parallel tasks
- Jobs specify resources (`--nodes`, `--ntasks`) in the script header
- **Parametric jobs** use arguments, env variables, or replacement symbols
- Requesting more `--ntasks` allows running multiple processes within one job
- Next session will cover **running parallel jobs across multiple nodes**

---

*Sources: Transcript `2026_03_03_SLURM (1)_7.md`*
