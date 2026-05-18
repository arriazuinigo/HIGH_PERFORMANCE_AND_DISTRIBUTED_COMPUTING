# High Performance & Distributed Computing — Session 17: Snakemake

**Date:** 2026-04-14 (Tue)
**Instructor:** Sandra Adriana Méndez (UAB)

---

## 1. Overview

This session introduces **Snakemake**, a workflow management system inspired by Make but designed to be more natural for bioinformatics pipelines. Snakemake is implemented in Python, making it more accessible to researchers across different fields.

---

## 2. Key Concepts

### 2.1 Why Snakemake Over Make?

| Aspect | Make | Snakemake |
|--------|------|-----------|
| **Implementation** | Shell-based | Python-based |
| **Target audience** | Computer science | Bioinformatics / research |
| **Readability** | Verbose syntax | Declarative, cleaner syntax |
| **File format** | Makefile | Snakefile |
| **Command** | `make` | `snakemake` |
| **Python integration** | None | Full Python in Snakefile |

**Core similarity:** Both rebuild only when dependencies change (incremental builds).

### 2.2 Snakemake Rules

Basic rule structure:
```python
rule count_words:
    input:
        "books/book1.txt"
    output:
        "results/book1.count"
    shell:
        "python scripts/countwords.py {input} > {output}"
```

- `input` — files required
- `output` — files produced
- `shell` — command to execute
- `{input}` / `{output}` — placeholders for file paths

### 2.3 Key Features

#### Parameters Section
- Dedicated `params` section for non-file parameters
- Example: `params: threshold=0.5`
- Referenced as `{params.threshold}` in shell commands

#### Configuration Files
- **Seperate config file** (`config.yaml`) stores settings (input paths, parameters)
- Accessed via `config["key"]` in Snakefile
- Single point of modification — change one file, not all rules

#### Parallel Execution
- `snakemake --cores N` — run N tasks in parallel
- `threads:` directive per rule for multi-threaded applications
- Example:
```python
rule my_tool:
    input: "in.txt"
    output: "out.txt"
    threads: 4
    shell: "my_tool -t {threads} {input} > {output}"
```

#### Integration with SLURM
- Snakemake supports SLURM via `--profile` or `--executor slurm`
- Run some rules locally, others on the cluster
- Configure SLURM parameters in a profile config file

### 2.4 Advanced Features

- **Multiple shell lines**: Use `run:` instead of `shell:` for Python code
- **Checkpointing**: Handle programs where output names are unknown beforehand
- **Combination with SLURM**: Define queue, job name, and other SLURM directives

---

## 3. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. Introduction** | 0:03–2:39 | Snakemake vs Make, Python integration |
| **II. Core Concepts** | 2:39–44:00 | Rules, input/output, params, config, threads |
| **III. SLURM Integration** | 44:00–52:59 | Running Snakemake on clusters |
| **IV. Closing** | 52:59–54:04 | Next session: hands-on example |

---

## 4. Key Takeaways

- **Snakemake** is the preferred workflow tool for bioinformatics
- Python-based → more **familiar and readable** than Make
- **Config files** centralize settings for maintainability
- **`--cores N`** enables parallel execution
- **SLURM profile** allows running workflows on HPC clusters
- Recommended for the **final assignment** instead of Make

---

*Sources: Transcript `2026_04_14_Snakemake_17.md`*
