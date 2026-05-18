# High Performance & Distributed Computing — Session 1: Course Presentation

**Date:** 2026-02-10 (Tue) · **Duration:** ~1h 27m (0:06–1:27:18)
**Instructors:** Miquel Àngel Senar Rosell (UAB), Sandra Adriana Méndez (UAB), Francesc Solsona Tehas (UdL)

> ⚠️ **Transcript Gap:** ~77 min missing (2:17–1:19:37). Core syllabus, evaluation details, SSH tutorial, and cluster setup were delivered during this interval. Content below is reconstructed from subsequent sessions and the course virtual page.

---

## 1. Grading & Assignments (from Campus Virtual)

### Gradebook Breakdown

| # | Assignment | Weight | Range | Due Date |
|---|-----------|--------|-------|----------|
| 1 | **Complexity Analysis Exercises** | 16.67 % | 0–10 | 2026-03-05 |
| 2 | **Recursive Programming Exercises** | 16.67 % | 0–10 | 2026-03-05 |
| 3 | **Middleware Assignment** | 16.67 % | 0–10 | 2026-05-04 |
| 4 | **Hands-On Lab 1 — HOL1** | 16.67 % | 0–10 | 2026-05-10 |
| 5 | **Hands-On Lab 2 — HOL2** | 16.67 % | 0–10 | 2026-05-31 |
| | **Quiz2** *(opens 2026-05-27 14:15, closes 22:10)* | — | — | 2026-05-27 |
| | **Total (known)** | **~83.35 %** | | |

> **Note:** The Campus Virtual gradebook lists 5 items at 16.67 % each. The original transcript estimated the Algorithmic Techniques block at ~35 %; actual breakdown may differ.

### Deliverable Formats

- **Option A:** `.zip` containing source code + PDF report
- **Option B:** Single Jupyter Notebook with embedded markdown explanations (no separate PDF)

Code must be runnable — instructors will test execution.

---

## 2. Course Structure — Three Blocks

```
HPC ──────────────────────────────────────────────────
├── 1. ALGORITHMIC TECHNIQUES & PROGRAMMING
│   ├── Complexity Analysis (Big O, linear/binary search)
│   ├── Recursive Programming
│   ├── Combinatorial Exploration & Backtracking
│   └── Dynamic Programming (memoization, tabulation, alignment)
│
├── 2. MIDDLEWARE & TOOLS
│   ├── Linux Processes (fg/bg, signals, ps, kill, xargs, parallel)
│   ├── SLURM (sbatch, arrays, dependencies, multi-node, MPI)
│   ├── Modules & Packages (os, subprocess, shutil, glob, BioPython)
│   ├── Make & Makefiles
│   └── Snakemake (workflows, SLURM integration)
│
└── 3. CLOUD COMPUTING (5 sessions)
    ├── Fundamentals & repositories
    ├── Cloud in healthcare, edge vs fog
    ├── Notebooks & cloud execution
    ├── Storage, buckets, Python file ops
    └── Advanced cloud services
```

---

## 3. Session Timeline

| Section | Time | Duration | What Happened |
|---------|------|----------|---------------|
| **I. Welcome** | 0:06–1:16 | ~1 min | Miquel Àngel introduces himself, Sandra Méndez & Francesc Solsona |
| **II. Overview** | 1:16–2:17 | ~1 min | Three-block structure outlined; starts describing Block 1 |
| *[GAP]* | *2:17–1:19:37* | *~77 min* | *Syllabus walkthrough, full evaluation, SSH tutorial, credentials* |
| **III. SSH Troubleshooting** | 1:19:37–1:27:01 | ~7 min | Hands-on support for students failing to connect |
| **IV. Close** | 1:27:01–1:27:18 | ~17 s | Session ends |

**Captured content:** ~10 min (gap obscures ~89 % of the lecture).

---

## 4. Detailed Summary

### 4.1 Welcome & Introduction (0:06–1:16)

- **Miquel Àngel Senar Rosell** (UAB) — main instructor
- **Sandra Adriana Méndez** (UAB) — co-instructor
- **Francesc Solsona Tehas** (UdL) — co-instructor
- Contact via institutional emails (UAB/UdL), **not** URV
- Earlier email sent re: cluster machine access

### 4.2 Course Overview (1:16–2:17)

Three main subjects:

1. **Algorithmic Techniques & Programming** — extends prior programming; foundation for Blocks 2 & 3
2. **Middleware** *(details in gap)*
3. **Cloud Computing** *(details in gap)*

### 4.3 SSH Connection Troubleshooting (1:19:37–1:27:01)

#### Connection Details

```bash
ssh username@machine_address          # primary
ssh -p <port> username@machine2       # secondary
```

- **Domains:** `.cat` and `.es` (synonyms)
- **Second machine** via `-p` flag
- **Username format:** `MHEDAS` + number
- **Cluster partitions:**
  - `aoclspv.uab.es:443` → partition `node.q` (recommended)
  - `aolin-login.uab.es:54022` → partition `cuda-ext.q`

#### Issues & Resolutions

| Problem | Fix / Status |
|---------|-------------|
| "Permission denied" | Password typo — check `l`/`I`/`0`/`O`/`1` |
| Connects to 2nd but not 1st machine | System admin issue — Miquel Àngel to investigate |
| "Connection closed" | System issue — escalated |
| Copy-paste from PDF fails | **Always type manually**, never paste |

#### Students Who Reported Issues

- Navdeep Kaur, Johanna Ursula Albers, Iris Mestres Pascual, Jan Carreras Boada, Noa-Sibila Janer Oliver

**Resolution:** Email Miquel Àngel directly; promised update by next session.

### 4.4 Closing (1:27:01–1:27:18)

No further issues raised. Recording stopped.

---

## 5. Instructors

| Name | Institution | Role |
|------|-------------|------|
| **Miquel Àngel Senar Rosell** | UAB | Main lecturer — Middleware & Tools |
| **Sandra Adriana Méndez** | UAB | Co-lecturer — Algorithmic Techniques |
| **Francesc Solsona Tehas** | UdL | Co-lecturer — Cloud Computing |

**Contact:** Use institutional email (UAB/UdL), not URV.

---

## 6. Block 1 — Algorithmic Techniques (reconstructed from Sessions 3+)

| Topic | Session | Key Points |
|-------|---------|-----------|
| **Complexity Analysis** | S3 (Feb 17) — Sandra | Big O, O(n) vs O(log n), empirical validation |
| **Recursive Programming** | S4 (Feb 18) | Recursion vs iteration; submission formats |
| **Combinatorial Exploration & Backtracking** | S8 (Mar 4) | Constraint-based recursion; Sudoku solver example |
| **Dynamic Programming** | S12–13 (Mar 18, 24) | Memoization, tabulation; sequence alignment with custom weights |

**Assignment:** Implement sequence alignment using memoization/tabulation with custom weights. *"Last assignment for this unit."*

---

## 7. Block 2 — Middleware (reconstructed from Sessions 2+)

| Topic | Sessions | Highlights |
|-------|----------|-----------|
| **Linux Processes** | S2 (Feb 11), S5 (Feb 24) | fg/bg, `ps`, `kill`, `xargs`, GNU `parallel` |
| **SLURM** | S7 (Mar 3), S9 (Mar 10) | `sbatch`, arrays, dependencies, MPI, 12 cores/node |
| **Modules & Packages** | S11 (Mar 17) — Miquel Àngel | `os`, `subprocess`, `shutil`, `glob`, BioPython |
| **Make & Makefiles** | S14 (Mar 25), S15 (Apr 7) | Variables, rules; count-primes pipeline example |
| **Snakemake** | S17 (Apr 14), S19 (Apr 21) | Rules, config, SLURM integration via `--cluster` / profiles v8+ |

---

## 8. Block 3 — Cloud Computing (Sessions by Francesc Solsona)

| Session | Date | Topic |
|---------|------|-------|
| S16 | Apr 8 | Fundamentals, repositories, basic concepts |
| S18 | Apr 15 | Healthcare cloud, edge vs fog, cell counting, remote monitoring |
| S20 | Apr 22 | Jupyter Notebooks in the cloud |
| S22 | Apr 29 | Buckets, storage, Python file operations |
| S23 | May 6 | Advanced cloud services |

---

## 9. Cluster Resources

| Resource | Details |
|----------|---------|
| **Connection** | SSH via `.cat` / `.es` domains |
| **Username** | `MHEDAS` + number |
| **Cores per node** | 12 |
| **Scheduler** | SLURM |
| **Partitions** | `node.q`, `cuda-ext.q` |
| **Credentials** | Shared across all machines |

---

## 10. Key Takeaways

- **5 graded assignments** (each 16.67 %, 0–10 scale)
- **3 course blocks** taught by 3 instructors
- **SSH + SLURM** are the core remote-work tools
- **Hands-on emphasis** — everything runs on the cluster
- **Academic integrity:** code must be runnable; submit as `.zip` + PDF or Jupyter Notebook

---

*Sources: Transcript `2026_02_10_Course Presentation_1.md`, Campus Virtual gradebook, sessions 2–23.*
