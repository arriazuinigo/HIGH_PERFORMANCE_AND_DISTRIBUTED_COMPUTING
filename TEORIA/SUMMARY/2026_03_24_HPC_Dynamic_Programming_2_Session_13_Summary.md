# High Performance & Distributed Computing — Session 13: Dynamic Programming (Part 2 — Tabulation)

**Date:** 2026-03-24 (Wed)
**Instructor:** Sandra Adriana Méndez (UAB)

---

## 1. Overview

This session concludes the Dynamic Programming topic by introducing **Tabulation** (bottom-up DP), **backtracking for Edit Distance**, and the final assignment.

---

## 2. Key Concepts

### 2.1 Tabulation (Bottom-Up DP)

| Aspect | Memoization | Tabulation |
|--------|-------------|------------|
| **Approach** | Top-down (recursive) | Bottom-up (iterative) |
| **Data structure** | Dictionary (cache) | Table (matrix) |
| **Start** | From the original problem | From the smallest subproblems |
| **Direction** | Recurse down, cache results | Build up from base cases |

**Tabulation process for Edit Distance:**
1. Create a matrix of size `(m+1) × (n+1)`
2. Fill the first row and column with base costs (insertions/deletions)
3. Fill each cell using the recurrence: min(insertion, deletion, substitution/match)
4. The final cell `[m][n]` = minimum Edit Distance

### 2.2 Edit Distance with Different Weights

- The basic algorithm uses cost = 1 for all operations
- **Real applications** may use different weights:
  - Match: +1 (reward)
  - Insertion: −4 (penalty)
  - Deletion: −4 (penalty)
- **Only the cost values change** — algorithm structure remains the same
- May also change from `min()` to `max()` depending on the scoring scheme

### 2.3 Backtracking (CIGAR)

- **CIGAR string** = sequence of operations that transforms one string into another
- Steps:
  1. Start from cell `[m][n]` (bottom-right)
  2. Trace back based on which neighbor was the source of the minimum
  3. Moving up = insertion; moving left = deletion; diagonal = match/substitution
  4. Reverse the result to get operations from start to end
- Returns: **Edit Distance** + **CIGAR string** + **matrix**

### 2.4 Complexity

- Both memoization and tabulation: **O(m × n)** — polynomial
- Tabulation uses iterative loops; memoization uses recursion + cache

---

## 3. Final Assignment

### 3.1 Task

- Implement Edit Distance using **either memoization or tabulation**
- Use **custom weights** for each operation (not all 1)
- Change `min()` to `max()` if required by the scoring scheme

### 3.2 What to Submit

- Source code implementing the algorithm with custom weights
- Demonstrate understanding of the DP structure

---

## 4. Summary of Algorithmic Techniques Block

| Technique | Key Idea | Typical Complexity |
|-----------|----------|-------------------|
| **Complexity Analysis** | Understand growth rates | — |
| **Recursive Programming** | Divide problem → similar subproblems | Varies |
| **Divide and Conquer** | Independent subproblems → combine | Often O(n log n) |
| **Combinatorial/Backtracking** | Explore solution space with pruning | Often exponential |
| **Dynamic Programming** | Cache subproblem results | Polynomial (O(m×n)) |

### 4.1 Key Philosophy

- Understand **complexity** to choose the right solution
- **Exponential is not good** — use DP to reduce complexity
- Python libraries are convenient, but understanding underlying algorithms is crucial
- The final assignment combines brute force (combinatorial) and DP approaches

---

## 5. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. Introduction** | 0:08–1:56 | Recap of memoization, Edit Distance |
| **II. Tabulation** | 32:37–35:15 | Bottom-up DP, matrix filling, CIGAR backtracking |
| **III. Custom Weights** | 35:15–37:44 | Applying DP with different operation costs |
| **IV. Final Assignment** | 37:44–40:21 | Assignment details and summary |
| **V. Closing** | 40:21–42:27 | Final thoughts on complexity importance |

---

## 6. Key Takeaways

- **Tabulation** = bottom-up DP using iterative matrix filling
- **Backtracking** extracts the sequence of operations (CIGAR)
- DP reduces exponential complexity to **polynomial**
- Custom weights can be applied **without changing algorithm structure**
- Understanding complexity is **critical** for selecting the right approach

---

*Sources: Transcript `2026_03_24_Dynamic Programming – Part 2_13.md`*
