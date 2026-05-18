# High Performance & Distributed Computing — Session 5: Linux Processes (2)

**Date:** 2026-02-24 (Tue)
**Instructor:** Miquel Àngel Senar Rosell (UAB)

---

## 1. Overview

This session continues from Session 2, covering advanced Linux process management tools: **xargs** and **GNU parallel**. These commands automate the execution of multiple parallel applications on a single machine.

---

## 2. Review: Foreground vs Background

### 2.1 Quick Recap

| Mode | Behavior |
|------|----------|
| **Foreground** | Process blocks terminal until completion |
| **Background (`&`)** | Process runs asynchronously; terminal remains free |
| **`jobs`** | Lists background processes |

---

## 3. New Tools

### 3.1 `xargs` — Execute Command Line Arguments in Parallel

**Purpose:** Manage execution of multiple parallel applications automatically.

**Key features:**
- Creates a list of tasks from input
- Manages and monitors applications automatically
- Starts new instances as previous ones complete

**Syntax example:**
```bash
seq 1 5 | xargs -n 1 -P 3 process
```
- `-n 1`: Take one argument at a time
- `-P 3`: Run up to 3 instances in parallel
- Input arguments come from standard input (piped)

**Argument substitution with `-I`:**
```bash
seq 1 5 | xargs -I {} process {}.gpj
```
- `-I {}`: Define placeholder for argument substitution
- Useful when argument position is not at the end

### 3.2 GNU `parallel` — Advanced Parallel Execution

**Purpose:** More powerful, modern alternative to `xargs` with richer syntax.

**Key features:**
- More flexible argument handling
- Arguments can come from: **command line**, **pipe**, or **file**
- Supports argument combinations
- More sophisticated syntax

**Examples:**

| Command | Behavior |
|---------|----------|
| `parallel -j 3 process ::: 1 2 3 4 5 6` | Run 6 instances, 3 at a time, args from command line |
| `parallel -j 3 process < input.txt` | Run instances, args from file |
| `parallel -j 3 process ::: 1 2 3 ::: A B C` | Generate all combinations (1A, 1B, 1C, 2A...) |
| `parallel -j 3 process ::: 1 2 3 :::+ A B C` | Pair arguments (1A, 2B, 3C) |

**Argument substitution with `{}`:**
```bash
parallel -j 3 process {} ::: 1 2 3
```

### 3.3 `xargs` vs `parallel`

| Feature | `xargs` | `parallel` |
|---------|---------|------------|
| Input source | Standard input only | stdin, command line, file |
| Argument placement control | `-I` flag | `{}` placeholder |
| Combinations | Manual | Built-in (`:::` / `:::+`) |
| Parallelism control | `-P` flag | `-j` flag |
| Modern features | Basic | Advanced |

---

## 4. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. Recap** | 0:06–2:12 | Review of foreground/background processes |
| **II. xargs** | 1:15:35–1:18:23 | xargs functionality and syntax |
| **III. GNU parallel** | 1:18:23–1:23:47 | Parallel command features and examples |
| **IV. Closing & Exercise** | 1:23:47–1:25:47 | Exercises and preview of next topic (SLURM) |

---

## 5. Homework / Exercise

- Practice using `xargs` and `parallel` on the cluster
- Experiment with different parallelism levels (`-P 3`, `-j 4`, etc.)
- Try different argument sources (stdin, file, command line)
- Explore argument combinations

---

## 6. Key Takeaways

- **xargs** and **parallel** automate parallel execution of multiple instances
- Both tools **manage job start/finish** automatically based on core availability
- **parallel** is more flexible with argument sources and combinations
- These tools work within a **single machine** (next topic: multi-machine via SLURM)
- Main advantage over manual `&` + `wait`: automatic resource management

---

*Sources: Transcript `2026_02_24_Linux Processes (2)_5.md`*
