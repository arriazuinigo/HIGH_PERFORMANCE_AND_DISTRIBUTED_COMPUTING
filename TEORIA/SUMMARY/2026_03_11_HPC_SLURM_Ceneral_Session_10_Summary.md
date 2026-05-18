# High Performance & Distributed Computing — Session 10: SLURM — General Meeting

**Date:** 2026-03-11 (Wed)
**Instructor:** Miquel Àngel Senar Rosell (UAB)

---

## 1. Overview

This wrap-up session on SLURM focuses on practical aspects of running multiple independent instances and distributing work across **multiple nodes** using `srun` inside batch scripts.

---

## 2. Key Concepts

### 2.1 Running Multiple Instances with `&` (ampersand)

- Inside a batch script, launch background processes with `&`
- **Important:** Must add `wait` at the end so the script doesn't exit before background processes finish
- Example:
```bash
#!/bin/bash
#SBATCH --ntasks=2
./my_app data1.txt &
./my_app data2.txt &
wait
```

### 2.2 Running Multiple Instances with `srun`

- `srun` automatically distributes tasks based on `--ntasks`
- Example:
```bash
#!/bin/bash
#SBATCH --ntasks=2
srun ./my_app
```
- This launches **2 instances** of `./my_app` (one per allocated task)

### 2.3 Distributing Different Work Across Nodes

More useful than running the same task multiple times:

```bash
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=1

srun --ntasks=1 ./process_a data_a.txt &
srun --ntasks=1 ./process_b data_b.txt &
wait
```

**Key points:**
- `--ntasks` in `sbatch` = total resources allocated
- `srun --ntasks=N` = how many of those resources to use for this specific command
- Multiple `srun` commands can distribute different work across allocated resources
- If `--ntasks=1` is specified in sbatch, only **one instance** will execute regardless of nodes

---

## 3. Live Demo: Practical Examples

### 3.1 Prime Counter Application

- Program that counts primes in a large range
- Running with `&` + `wait`: 2 instances run in parallel, using 2 cores
- Running with `srun`: Same effect but SLURM-managed

### 3.2 Key Observations

- `srun` with `--ntasks=2` runs 2 instances on the 2 allocated cores
- Without `wait`, the script exits immediately and orphaned background processes
- Number of `--ntasks` controls how many `srun` instances are created

---

## 4. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. Recap** | 0:04–2:18 | Review of SLURM parameters, hybrid program example |
| **II. Live Demo** | 42:17–51:45 | Practical examples with prime counter, `&`, `srun` |
| **III. Multi-node distribution** | 51:45–52:38 | Distributing work across nodes with `srun` |
| **IV. Closing** | 52:38–53:45 | Final questions |

---

## 5. Key Takeaways

- **`&` + `wait`** = simplest way to run parallel instances inside a batch script
- **`srun`** = SLURM-aware way to launch tasks across allocated resources
- `--ntasks` in sbatch = total resources; `srun` distributes across them
- Without `wait`, the script exits prematurely
- Multiple `srun` calls can distribute **different** workloads

---

*Sources: Transcript `2026_03_11_Reunión en General_10.md`*
