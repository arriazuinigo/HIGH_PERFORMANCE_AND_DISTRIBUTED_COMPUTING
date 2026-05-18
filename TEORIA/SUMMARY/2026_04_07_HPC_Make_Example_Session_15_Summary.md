# High Performance & Distributed Computing — Session 15: Make Example

**Date:** 2026-04-07 (Wed)
**Instructor:** Sandra Adriana Méndez (UAB)

---

## 1. Overview

This hands-on session walks through building a **Makefile step by step** for the Zipf's Law analysis pipeline, demonstrating how to evolve from a basic version to a fully-featured one with variables, patterns, and help functionality.

---

## 2. Building the Makefile

### 2.1 Basic Version

- Start with the exact **command line** used to run the pipeline
- Define **target** (output) and **dependency** (input files)
- Example:
```makefile
results.txt: books/*.txt
	python countwords.py books/*.txt > results.txt
```

### 2.2 Using Variables

- Define variables for scripts, data paths, and options
- Improves readability and maintainability
- Example:
```makefile
SCRIPTS = scripts
DATA = books
OUTPUT = results

$(OUTPUT)/results.txt: $(DATA)/*.txt
	python $(SCRIPTS)/countwords.py $^ > $@
```

### 2.3 Automatic Variables

| Variable | Meaning |
|----------|---------|
| `$@` | Target name |
| `$<` | First dependency |
| `$^` | All dependencies |
| `$*` | Stem of the pattern match |

### 2.4 Pattern Rules

- Use `%` wildcard to create generic rules
- Ideal for processing **multiple files** with the same recipe
- Example:
```makefile
$(OUTPUT)/%.count: $(DATA)/%.txt
	python $(SCRIPTS)/countwords.py $< > $@
```

### 2.5 Adding Help

- **Help is NOT automatic** — must be explicitly defined
- Add comments before each target
- Use a `help` target that parses these comments
- Example:
```makefile
help:          ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*##' $(MAKEFILE_LIST) | sort
```

### 2.6 Clean Target

- Remove all generated files
- Useful for fresh rebuilds
- Should be declared as `.PHONY` (not a real file)

### 2.7 Final Extended Version

- Includes all targets: **results**, **plots**, **clean**, **help**
- Uses **config file** (`config.mk`) for centralized settings
- Takes advantage of **incremental builds** — only re-runs steps where inputs changed

---

## 3. Key Takeaways

- Start with a **simple command line** → evolve into a Makefile
- **Variables** make Makefiles reusable and maintainable
- **Pattern rules** (`%`) handle multiple files elegantly
- **Help** must be explicitly defined — not automatic
- **Incremental builds** are Make's core advantage
- Practice by running on the **cluster** to prepare for Snakemake

---

*Sources: Transcript `2026_04_07_Make Example_15.md`*
