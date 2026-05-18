# High Performance & Distributed Computing — Session 19: Snakemake Example

**Date:** 2026-04-21 (Tue)
**Instructor:** Sandra Adriana Méndez (UAB)

---

## 1. Overview

This hands-on session walks through the **Zipf's Law analysis pipeline** using Snakemake, including practical execution on the cluster with SLURM integration.

---

## 2. The Pipeline

### 2.1 Three Steps

1. **Count words** in each book (10 books) → 10 individual count files
2. **Plot** word frequencies for each book
3. **Test Zipf's Law** across all books

### 2.2 Snakemake Rules

**Basic rule (no wildcards):**
```python
rule count_words:
    input: "books/book1.txt"
    output: "results/book1.count"
    shell: "python scripts/countwords.py {input} > {output}"
```

**With wildcards (generic for all books):**
```python
rule count_words:
    input: "books/{book}.txt"
    output: "results/{book}.count"
    shell: "python scripts/countwords.py {input} > {output}"
```

---

## 3. SLURM Integration

### 3.1 Two Approaches

**Approach 1: Profile configuration**
- Create a `slurm` folder with a `config.yaml` file
- Parameters: `jobs`, `latency-wait`, `partition`, nodes, tasks, etc.

```yaml
jobs: 10
latency-wait: 60
partition: "compute"
nodes: 1
```

**Approach 2: Direct executor (`--executor slurm`)**
- Newer Snakemake versions (v7+)
- Requires plugin installation

### 3.2 Running on Cluster

```bash
snakemake --profile slurm --cores 4
```

- Snakemake submits each rule as a SLURM job
- **Latency-wait** handles filesystem delays (important for network storage)
- Output appears incrementally as jobs complete

### 3.3 Practical Demo Issues

- File system latency caused errors during the demo
- **Solution:** Increase `latency-wait` (e.g., 60 seconds instead of 20)
- SLURM integration is powerful but debugging can be complex

---

## 4. Recommendation for Final Assignment

- **Snakemake** is preferred over Make for the final assignment
- More relevant for bioinformatics/data science
- Students should practice connecting to the cluster and testing Snakemake

### 4.1 Cluster Access

- All students have accounts to connect to the cluster
- Activate Snakemake via Conda
- Copy example files from shared directory to personal home

---

## 5. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. Introduction** | 0:51–3:10 | Pipeline overview, three steps |
| **II. Snakefile Walkthrough** | 3:10–40:36 | Building rules, wildcards, config |
| **III. SLURM Integration** | 40:36–48:42 | Profile, executor, live demo on cluster |
| **IV. Recommendations** | 48:42–51:46 | Practice advice, final assignment |

---

## 6. Key Takeaways

- Start with **simple rules** → evolve with wildcards and config
- **Wildcards** (`{book}`) handle multiple input files elegantly
- **SLURM profile** configures cluster submission
- **Latency-wait** is crucial for network filesystems
- Practice on the **cluster** to prepare for the final assignment

---

*Sources: Transcript `2026_04_21_Snakemake Example_19.md`*
