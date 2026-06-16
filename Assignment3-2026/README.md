# Assignment 3 — Reproducible Sequence Analysis Pipeline

## Overview

A fully reproducible bioinformatics pipeline that analyses 50 *Papilio machaon* DNA sequences from `PM_50.fasta`. The workflow applies **Dynamic Programming**, **Regular Expressions**, **Conda environments**, and **Snakemake** to extract sequence information, compute pairwise edit-distance alignments, generate CIGAR strings, and summarise the results.

---

## Requirements

| Part | Topic | Points |
|------|-------|--------|
| 1 | FASTA parsing with Regular Expressions | 1.5 |
| 2 | Dynamic Programming edit distance | 3.5 |
| 3 | CIGAR string generation via traceback | 2.0 |
| 4 | Regex analysis of CIGAR strings + report | 1.0 |
| 5 | Conda environment | 1.0 |
| 6 | Snakemake workflow automation | 1.0 |

**General constraints:** Python 3 only, no external bioinformatics libraries (e.g. Biopython), all outputs in TSV format, all file names exactly as specified.

---

## Input Data

| File | Description |
|------|-------------|
| `PM_50.fasta` | 50 unplaced genomic scaffolds from *Papilio machaon* (Pap_ma_1.0 assembly). Mixed-case sequences — uppercase regions are repeat-masked. Sequence lengths range from ~1 100 to ~1 200 bp. |

---

## Pipeline Architecture

```
PM_50.fasta
     │
     ▼
parse_fasta.py  ──►  sequences.tsv
     │
     ▼ (also reads PM_50.fasta directly)
alignment.py    ──►  distances.tsv
                ──►  alignments.tsv
                         │
                         ▼
               cigar_stats.py  ──►  cigar_stats.tsv
                               ──►  report.txt
```

The entire pipeline is automated by **Snakemake** (`Snakefile`) and can be reproduced in a single command:

```bash
snakemake --cores 1
```

---

## Part-by-Part Analysis

### Part 1 — FASTA Parsing (`parse_fasta.py`)

**Approach:**  
- Read the file line by line.  
- Detect header lines with the regex `^>(\S+)` — the first non-whitespace token after `>` is the accession identifier.  
- Concatenate all subsequent lines until the next header to reconstruct each complete sequence.  
- Write one row per sequence to `sequences.tsv`.

**Key technique:** `re.compile(r'^>(\S+)')` — anchored to the start of the line, captures the accession without hard-coding any expected format.

**Output — `sequences.tsv`** (50 rows, tab-separated):

```
Accession       Length
NW_014478584.1  1188
NW_014478585.1  1116
...
```

---

### Part 2 — Dynamic Programming Edit Distance (`alignment.py`)

**Reference sequence:**  
The first 18 nucleotides of the first record, extracted automatically and uppercased:  
`AAGTTAAGATAAAAACAA`

**Algorithm — `edit_distance_dp(pattern, text)`:**  
Bottom-up tabulation over an (n+1)×(m+1) matrix where cell **M\[i\]\[j\]** stores the minimum edit distance between `pattern[0:i]` and `text[0:j]`.

Initialisation:
- `M[i][0] = i` — deleting all i characters of pattern to reach empty string  
- `M[0][j] = j` — inserting j characters to build text from empty string

Recurrence:
```
cost = 0  if  pattern[i-1] == text[j-1]  else  1
M[i][j] = min(
    M[i-1][j-1] + cost,   # diagonal: match (0) or substitution (1)
    M[i-1][j]   + 1,      # up:       deletion
    M[i][j-1]   + 1,      # left:     insertion
)
```

**Why DP avoids redundant work:** A naïve recursive solution recomputes the same sub-problems `(i, j)` exponentially many times. By storing every result in the matrix, each of the (n+1)×(m+1) cells is filled exactly once → **O(n·m)** time and space.

**DP matrix for the first sequence (self-alignment, distance = 0):**

```
          A   A   G   T   T   A   A   G   A   T   A   A   A   A   A   C   A   A
       -----------------------------------------------------------------------
     |  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18
  A  |  1   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
  A  |  2   1   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
  G  |  3   2   1   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
  T  |  4   3   2   1   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14
  T  |  5   4   3   2   1   0   1   2   3   4   5   6   7   8   9  10  11  12  13
  A  |  6   5   4   3   2   1   0   1   2   3   4   5   6   7   8   9  10  11  12
  A  |  7   6   5   4   3   2   1   0   1   2   3   4   5   6   7   8   9  10  11
  G  |  8   7   6   5   4   3   2   1   0   1   2   3   4   5   6   7   8   9  10
  A  |  9   8   7   6   5   4   3   2   1   0   1   2   3   4   5   6   7   8   9
  T  | 10   9   8   7   6   5   4   3   2   1   0   1   2   3   4   5   6   7   8
  A  | 11  10   9   8   7   6   5   4   3   2   1   0   1   2   3   4   5   6   7
  A  | 12  11  10   9   8   7   6   5   4   3   2   1   0   1   2   3   4   5   6
  A  | 13  12  11  10   9   8   7   6   5   4   3   2   1   0   1   2   3   4   5
  A  | 14  13  12  11  10   9   8   7   6   5   4   3   2   1   0   1   2   3   4
  A  | 15  14  13  12  11  10   9   8   7   6   5   4   3   2   1   0   1   2   3
  C  | 16  15  14  13  12  11  10   9   8   7   6   5   4   3   2   1   0   1   2
  A  | 17  16  15  14  13  12  11  10   9   8   7   6   5   4   3   2   1   0   1
  A  | 18  17  16  15  14  13  12  11  10   9   8   7   6   5   4   3   2   1   0
```

The diagonal of zeros confirms the self-alignment has distance 0.

**Output — `distances.tsv`** (50 rows):

```
Accession       Distance
NW_014478584.1  0
NW_014478585.1  10
...
```

---

### Part 3 — CIGAR Generation (`alignment.py`)

**Traceback procedure (`traceback_cigar`):**  
Starting from `M[n][m]`, move backwards to `M[0][0]` applying priority: diagonal > up > left.

| Movement | Operation | Meaning |
|----------|-----------|---------|
| Diagonal, chars equal | `M` | Match |
| Diagonal, chars differ | `X` | Substitution |
| Up (`i` decreases) | `D` | Deletion in query |
| Left (`j` decreases) | `I` | Insertion in query |

Operations are collected in reverse and flipped to produce the forward CIGAR string.

**Output — `alignments.tsv`** (50 rows):

```
Accession       Distance  CIGAR
NW_014478584.1  0         MMMMMMMMMMMMMMMMMM
NW_014478585.1  10        DXXMMXXMMMMMXXXXMIM
NW_014478586.1  10        XXXMMMIXXMMXXMXMDMM
...
```

---

### Part 4 — CIGAR Statistics & Report (`cigar_stats.py`)

**Approach:** For each CIGAR string, `re.findall(r'M', cigar)` (and equivalently for `I`, `D`, `X`) counts every occurrence of that operation character. This is far more concise than a manual loop and directly expresses the intent.

**Why regex is useful in bioinformatics formats:**  
Formats like FASTA headers, CIGAR strings, SAM/VCF fields, and GenBank annotations are line- or field-based structured text. Regular expressions let you extract, validate, and count patterns in a single expression without writing custom parsers — making the code shorter, readable, and less error-prone.

**Output — `cigar_stats.tsv`** (50 rows):

```
Accession       M   I   D   X
NW_014478584.1  18  0   0   0
NW_014478585.1   9  1   1   8
...
```

**Output — `report.txt`:**

```
Sequence with smallest edit distance:
NW_014478584.1  |  Distance: 0  |  M:18  I:0  D:0  X:0

Sequence with largest edit distance:
NW_014478593.1  |  Distance: 15  |  M:5  I:2  D:2  X:11

Sequence with largest number of matches:
NW_014478584.1  |  Distance: 0  |  M:18  I:0  D:0  X:0
```

---

### Part 5 — Conda Environment (`environment.yml`)

```yaml
name: assignment3
channels:
  - conda-forge
  - bioconda
  - defaults
dependencies:
  - python=3.10
  - snakemake-minimal=7.32.4
  - pip
```

| Command | Purpose |
|---------|---------|
| `conda env create -f environment.yml` | Create the environment |
| `conda activate assignment3` | Activate it |
| `conda env export > environment.yml` | Export it |

All three Python scripts use only the **standard library** (`re`, `sys`) so no extra packages are needed beyond Python and Snakemake itself. The environment file guarantees any collaborator can recreate an identical software stack and obtain the same results.

---

### Part 6 — Snakemake Workflow (`Snakefile`)

```
rule all   →  report.txt                        (final target)
rule parse →  PM_50.fasta          → sequences.tsv
rule align →  PM_50.fasta + ↑      → distances.tsv + alignments.tsv
rule stats →  alignments.tsv + ↑   → cigar_stats.tsv + report.txt
```

Snakemake infers the execution order automatically from the dependency graph. If an input file changes, only the downstream rules re-run — avoiding unnecessary recomputation. This makes the workflow **deterministic**, **auditable**, and **portable**.

**`snakemake -n` dry-run output (all 4 jobs planned):**

```
job      count
-----  -------
parse        1
align        1
stats        1
all          1
total        4
```

**DAG image:** `dag.png` (generated with `snakemake --dag | dot -Tpng > dag.png`)

---

## Results Summary

| Metric | Value |
|--------|-------|
| Sequences analysed | 50 |
| Reference (first 18 nt) | `AAGTTAAGATAAAAACAA` |
| Minimum edit distance | **0** — `NW_014478584.1` (self, 18 matches) |
| Maximum edit distance | **15** — `NW_014478593.1` (5M, 2I, 2D, 11X) |
| Mean edit distance | **10.56** |
| Most frequent distance | 10 (13 sequences) |
| Most matches | 18 — `NW_014478584.1` |

**Distance distribution across 50 sequences:**

| Distance | # Sequences |
|----------|-------------|
| 0 | 1 |
| 6 | 1 |
| 7 | 3 |
| 8 | 2 |
| 9 | 6 |
| 10 | 13 |
| 11 | 5 |
| 12 | 8 |
| 13 | 5 |
| 14 | 5 |
| 15 | 1 |

The high mean distance (~10.56 out of 18 positions) reflects the biological diversity expected between unrelated genomic scaffolds — the 18-nt window is drawn from a non-coding region with no conservation pressure.

---

## Deliverables

```
assignment3/
├── PM_50.fasta          input sequences
├── parse_fasta.py       Part 1 – FASTA parser
├── alignment.py         Parts 2 & 3 – DP alignment + CIGAR
├── cigar_stats.py       Part 4 – CIGAR stats & report
├── Snakefile            Part 6 – workflow automation
├── environment.yml      Part 5 – Conda environment spec
├── sequences.tsv        output: accession + length
├── distances.tsv        output: edit distances
├── alignments.tsv       output: distances + CIGAR strings
├── cigar_stats.tsv      output: per-sequence CIGAR stats
├── report.txt           output: summary report
├── dag.png              output: Snakemake workflow DAG
└── answers.pdf          conceptual answers (manual)
```


