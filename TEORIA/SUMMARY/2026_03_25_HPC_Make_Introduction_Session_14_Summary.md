# High Performance & Distributed Computing — Session 14: Workflow Management — Make Introduction

**Date:** 2026-03-25 (Wed)
**Instructor:** Sandra Adriana Méndez (UAB)

---

## 1. Overview

This session introduces **Workflow Management Systems**, starting with the **Make** tool. Make automates the execution of multi-step pipelines, ensuring robustness, reproducibility, and incremental execution.

---

## 2. Key Concepts

### 2.1 Why Workflow Management?

Processing biomedical data involves **multi-step pipelines**:
1. Filter raw data
2. Curate/clean
3. Compare with databases
4. Generate output

**Desired characteristics of a workflow tool:**
| Characteristic | Description |
|----------------|-------------|
| **Robustness** | Handle errors gracefully, provide recovery |
| **Reproducibility** | Same inputs → same outputs every time |
| **Incrementality** | Only re-run steps where inputs changed |

### 2.2 Make Fundamentals

- **Makefile** defines rules with **targets**, **dependencies**, and **commands**
- **Rules:** Only re-execute if dependencies are newer than target
- **Syntax:**
```makefile
target: dependencies
	command
```

### 2.3 Makefile Variables

```makefile
CC = gcc
CFLAGS = -O2
TARGET = myprogram

$(TARGET): main.o utils.o
	$(CC) $(CFLAGS) -o $(TARGET) main.o utils.o
```

### 2.4 Conditionals in Make

- Control compilation options based on environment
- Example: Use different flags depending on the hostname (local vs cluster)
- `ifdef`, `ifeq`, `ifneq` directives

### 2.5 Parallel Execution with Make

- `make -j N` — run up to N tasks in parallel
- Useful for long-running pipelines
- Number of parallel tasks typically = number of cores available

---

## 3. Practical Exercise: Zipf's Law Analysis

### 3.1 The Pipeline

1. **Count words** in text files (books) → generate word frequency files
2. **Summarize** frequencies → check ratios
3. **Plot** results → visualize

### 3.2 Goal

- Create a **Makefile** that automates all pipeline steps
- Practice defining targets, dependencies, and rules
- Test locally or on the cluster

---

## 4. Limitations of Make

- Managing **complex inputs** (many files, folders) is difficult
- For **large-scale pipelines**, Make may not be the best option
- However, it's **simple to learn** and useful for small-to-medium workflows

---

## 5. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. Introduction** | 0:08–2:09 | Workflow management concepts |
| **II. Make Overview** | 2:09–1:03 | Make syntax, variables, conditionals |
| **III. Demo/Live** | 1:03–1:09 | Live Makefile example on cluster |
| **IV. Exercises** | 1:09–1:13 | Zipf's Law analysis exercise |

---

## 6. Key Takeaways

- **Make** is a simple but effective workflow management tool
- **Targets + dependencies** define when to rebuild
- **Variables** avoid repetition; **conditionals** adapt to environments
- **`-j N`** enables parallel execution
- Suitable for simple pipelines; more complex tools (Snakemake) coming next

---

*Sources: Transcript `2026_03_25_Make_14.md`*
