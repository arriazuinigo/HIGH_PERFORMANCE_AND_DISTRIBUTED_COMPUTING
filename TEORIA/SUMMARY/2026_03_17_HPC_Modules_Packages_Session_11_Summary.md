# High Performance & Distributed Computing — Session 11: Modules & Packages

**Date:** 2026-03-17 (Wed)
**Instructor:** Miquel Àngel Senar Rosell (UAB)

---

## 1. Overview

This session covers two main topics: **Python modules and packages theory**, and a review of the **most useful Python modules** for bioinformatics and biomedical data analysis workflows.

---

## 2. Key Concepts

### 2.1 Biomedical Data Workflows

- Analyzing biomedical data is **not a single step** — it involves filtering, curating, matching, comparing with databases
- Workflows require applications that control multiple steps
- Emphasis on tools for developing workflows that process biomedical data from input to informative output

### 2.2 File Manipulation Modules

#### `os` and `os.path` / `pathlib`

| Method | Description |
|--------|-------------|
| `os.getcwd()` | Get current working directory |
| `os.chdir(path)` | Change directory |
| `os.listdir(path)` | List files in directory (returns list) |
| `os.scandir(path)` | List files with additional info (iterator) |
| `os.walk(path)` | Traverse directory tree recursively |
| `os.mkdir()` / `os.makedirs()` | Create directories |
| `os.rename()` | Rename files/folders |

**File attributes available via `os.stat()`:**
- File name, size, creation time
- Owner user and group
- Many other metadata attributes

#### `shutil` — High-level File Operations

- `shutil.copy()` — Copy files
- `shutil.copytree()` — Copy entire directory tree
- `shutil.move()` — Move/rename files
- `shutil.rmtree()` — Remove entire directory tree

#### `glob` — Pattern-based File Matching

- Find files matching patterns: `glob.glob("*.txt")`, `glob.glob("**/*.csv", recursive=True)`

### 2.3 BioPython (Preview)

- **BioPython** is a major package for biological sequence manipulation
- Supports multiple sequence formats (FASTA, GenBank, etc.)
- Access to NCBI databases remotely
- Modules for: **phylogenetics**, **proteomics**, sequence alignment
- To be covered after Easter holidays

### 2.4 Other Utility Modules

| Module | Purpose |
|--------|---------|
| `subprocess` | Run system commands from Python |
| `sys` | System-specific parameters and functions |
| `tempfile` | Generate temporary files/folders |
| `zipfile` / `tarfile` | File compression and archiving |

---

## 3. Key Takeaways

- Python modules provide reusable components for building data analysis workflows
- `os` + `shutil` + `glob` cover most file/folder manipulation needs
- **BioPython** is essential for sequence data in bioinformatics
- No single module solves everything — choose the right tool for each operation
- Most common operations are covered by the methods listed in this session

---

*Sources: Transcript `2026_03_17_Modules & Packages_11.md`*
