# High Performance & Distributed Computing — Session 9: SLURM (2)

**Date:** 2026-03-10 (Tue)
**Instructor:** Miquel Àngel Senar Rosell (UAB)

---

## 1. Overview

This session continues with SLURM, focusing on **parallel programming models** (shared memory vs distributed memory) and how to request the correct resources for each type of application.

---

## 2. Key Concepts

### 2.1 Parallel Programming Models

#### Shared Memory Model (OpenMP)

| Characteristic | Description |
|----------------|-------------|
| **Mechanism** | Multiple threads share the same memory space |
| **Scope** | Single machine / single node |
| **Middleware** | OpenMP (directives in code) |
| **Granularity** | Fine-grained (loop-level parallelism) |

**Example:** Computing an integral by dividing rectangles:
- Loop over all rectangles to compute area
- With OpenMP: split loop into 4 sub-loops, each thread computes a portion
- All threads access same variable `sum` → needs synchronization

#### Distributed Memory Model (MPI)

| Characteristic | Description |
|----------------|-------------|
| **Mechanism** | Multiple processes exchange messages |
| **Scope** | Multiple nodes (distributed cluster) |
| **Middleware** | MPI (Message Passing Interface) |
| **Granularity** | Coarse-grained |

**Key difference:** Processes do NOT share memory — they communicate via explicit messages (send/receive)

### 2.2 Hybrid Model

- **Combination** of OpenMP (within a node) + MPI (across nodes)
- Application can use multiple nodes AND multiple cores per node
- Requires careful resource specification in SLURM

### 2.3 Mapping Resources to SLURM

| Application Type | SLURM Directives |
|-----------------|------------------|
| **Single-core sequential** | `--nodes=1 --ntasks=1 --cpus-per-task=1` |
| **OpenMP (shared memory)** | `--nodes=1 --cpus-per-task=12` (or however many threads) |
| **MPI (distributed)** | `--nodes=4 --ntasks=4 --cpus-per-task=1` |
| **Hybrid** | `--nodes=4 --ntasks=4 --cpus-per-task=12` |

### 2.4 Important Note

- The `--ntasks` directive correlates to the number of instances `srun` will launch
- If you request `--nodes=2` but only `--ntasks=1`, only one node will be used — the other remains idle
- If you want to distribute work across nodes, request enough `--ntasks`

---

## 3. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. Introduction** | 0:31–1:09 | Recap of single-machine tools, shift to multi-machine |
| **II. Shared Memory (OpenMP)** | 1:09:46–1:11:24 | Thread model, loop parallelism, synchronization |
| **III. Distributed Memory (MPI)** | 1:11:24–1:13:01 | Message passing, communication middleware |
| **IV. Hybrid Model** | 1:13:01–1:14:56 | Combining OpenMP + MPI |
| **V. Resource Mapping** | 1:14:56–1:16:48 | Linking application architecture to SLURM directives |
| **VI. Closing** | 1:16:48–1:19:36 | Exercises and preview |

---

## 4. Homework / Exercises

- Practice with **array jobs** and **job dependencies** (from transparencies)
- Experiment with different resource requests (`--nodes`, `--ntasks`, `--cpus-per-task`)
- Try running OpenMP or MPI applications if available

---

## 5. Key Takeaways

- **Shared memory (OpenMP):** multiple threads, single node, shared data
- **Distributed memory (MPI):** multiple processes, multiple nodes, messages
- **Hybrid:** combine both for maximum parallelism
- SLURM must be told the **architecture** of your application to allocate correctly
- `--ntasks` controls how many instances `srun` launches
- Understanding application documentation is key to knowing what resources to request

---

*Sources: Transcript `2026_03_10_SLURM (2)_9.md`*
