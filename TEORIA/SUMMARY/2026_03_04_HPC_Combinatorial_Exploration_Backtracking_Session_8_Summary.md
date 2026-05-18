# High Performance & Distributed Computing — Session 8: Combinatorial Exploration and Backtracking

**Date:** 2026-03-04 (Wed)
**Instructor:** Sandra Adriana Méndez (UAB)

---

## 1. Overview

This session covers **Combinatorial Exploration** and **Backtracking**, two related algorithmic techniques for solving complex problems where subproblems are **not independent** (unlike Divide and Conquer). These techniques explore a solution space by generating and testing all possible combinations.

---

## 2. Key Concepts

### 2.1 Combinatorial Exploration vs Divide & Conquer

| Aspect | Divide & Conquer | Combinatorial Exploration / Backtracking |
|--------|-----------------|----------------------------------------|
| **Subproblems** | Independent | Interdependent / related |
| **Solution space** | Deterministic | Large, explorative |
| **Complexity** | Often polynomial | Often exponential |
| **Approach** | Split, solve, combine | Generate, test, prune |

### 2.2 Combinatorial Exploration

- **Goal:** Explore all possible combinations or permutations of a given set of elements
- **Approach:** Exhaustive search of the entire solution space
- **Complexity:** Exponential — depends on number of elements and all possible solutions
- Usually implemented with **recursion**

### 2.3 Backtracking

- **Goal:** Find solution(s) subject to constraints
- **Approach:** Build solution incrementally; abandon ("backtrack") as soon as a constraint is violated
- **Pruning:** Stop exploring a branch once it's determined to be invalid
- More efficient than pure combinatorial exploration when constraints are tight

### 2.4 Examples Covered

#### String Permutations
- Generate all possible permutations of characters in a string
- Swapping technique to generate unique combinations

#### Sudoku Solver
- **Constraint check:** Each row, column, and 3×3 square must contain unique numbers 1–9
- **Validation function:** Check if placing a number violates constraints
- **Recursive search:** Try numbers, recurse, backtrack if stuck
- The recursive structure:
  1. Find an empty cell
  2. Try a valid number (1–9) that passes constraint check
  3. Recursively solve the rest
  4. If recursion fails, backtrack (reset cell) and try next number
  5. Return `True` when completely solved

---

## 3. Assignment Status & Q&A

### 3.1 Submission Guidelines

- Upload **source code** (preferably as `.py` files) + **PDF explanation**
- Or upload a **Jupyter Notebook** with code + markdown explanations
- Screenshots of code in PDF are **not sufficient** — instructor needs to run the code

### 3.2 Grading

- Algorithmic Techniques block = **35% of total grade**
- Includes: Complexity Analysis, Recursive Programming, Divide and Conquer, Combinatorial/Backtracking, Dynamic Programming
- The final assignment will be more complex with more weight

### 3.3 Q&A Highlights

- **Ludovic:** Can we just put screenshots of code in PDF? → **No**, source code must be provided so it can be run
- **Navdeep:** Can we submit separate files (PDF + .py) instead of a zip? → **Yes**, either way is fine

---

## 4. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. Introduction** | 0:03–2:10 | Combinatorial exploration vs Divide & Conquer |
| **II. Permutations** | 2:10–2:47 | String permutation example |
| **III. Sudoku Solver** | 45:05–48:04 | Backtracking validation + recursive backtracking |
| **IV. Q&A** | 48:04–54:01 | Assignment submission details and grading |

---

## 5. Key Takeaways

- **Combinatorial exploration** = exhaustive search of all possibilities (expensive)
- **Backtracking** = search with pruning (more efficient where constraints exist)
- Backtracking is ideal for constraint satisfaction problems (Sudoku, N-Queens, etc.)
- **Pruning** is key: detect invalid branches as early as possible
- Complexity is often **exponential** — understand when to use these techniques

---

*Sources: Transcript `2026_03_04_Combinatorial Exploration and Backtracking_8.md`*
