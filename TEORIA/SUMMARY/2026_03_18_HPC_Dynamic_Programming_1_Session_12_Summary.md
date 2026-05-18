# High Performance & Distributed Computing — Session 12: Dynamic Programming (Part 1)

**Date:** 2026-03-18 (Wed)
**Instructor:** Sandra Adriana Méndez (UAB)

---

## 1. Overview

This session introduces **Dynamic Programming (DP)**, the last algorithmic technique in this block. The focus is on understanding DP through **memoization** (top-down approach), using the Fibonacci sequence and the **Edit Distance** problem as examples.

---

## 2. Key Concepts

### 2.1 Why Dynamic Programming?

- **Problem:** Naive recursive solutions (e.g., Fibonacci) do **duplicate work** — same subproblems recalculated multiple times
- **Solution:** Store results of subproblems and reuse them → **Dynamic Programming**
- **Result:** Reduce exponential complexity to **polynomial complexity**

### 2.2 Fibonacci Example

| Approach | Complexity | Behavior |
|----------|------------|----------|
| Naive recursion | O(2ⁿ) | Exponential — each call spawns 2 more calls |
| DP (memoization) | O(n) | Linear — each value computed once, stored, reused |

### 2.3 Memoization (Top-Down DP)

- **Idea:** Add a **dictionary** (cache) to store computed results
- **Check at beginning:** If result already in cache → return it (no recomputation)
- **Store at end:** Before returning, save result in cache
- **Rule of thumb:** Always check at the beginning; always store at the end

---

## 3. Edit Distance Problem

### 3.1 Problem Definition

- **Goal:** Compute the minimum cost to transform one string into another
- **Operations:** Substitution, Insertion, Deletion (each has cost = 1 by default)
- **Application:** Sequence alignment in bioinformatics (DNA/protein comparison)

### 3.2 Naive Solution

- **Combinatorial search** — exponential complexity
- Explores all possible sequences of operations
- Impractical for long strings

### 3.3 DP Solution with Memoization

- **Cache key:** Combination of `(pattern_index, text_index)` — represents the substring pair being compared
- **Check:** If key exists in dictionary → return stored value
- **Compute:** Run the recursive algorithm normally
- **Store:** Save result before returning

### 3.4 Complexity

- **Memoized Edit Distance:** O(m × n) — polynomial
- Where `m` = length of pattern, `n` = length of text
- Dramatically better than exponential

---

## 4. Final Assignment Preview

- The final DP assignment will ask to **modify the Edit Distance algorithm**
- Change operation costs (match, insertion, deletion) to different values
- The algorithm structure remains the same — only cost values change
- **Key:** Understand the memoization pattern (check + compute + store)

---

## 5. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. Introduction** | 0:03–2:16 | Dynamic Programming concept, Fibonacci motivation |
| **II. Memoization** | 29:39–35:54 | Cache structure, Edit Distance with memoization |
| **III. Assignment & Q&A** | 35:54–39:57 | Final assignment preview, student questions |

---

## 6. Key Takeaways

- **Dynamic Programming** eliminates duplicate work by caching results
- **Memoization** = top-down DP with recursion + dictionary
- Edit Distance DP reduces complexity from **exponential to polynomial**
- Always: **check** cache at start → **store** result at end
- The final assignment will involve **changing operation costs** in the Edit Distance algorithm

---

*Sources: Transcript `2026_03_18_Dynamic Programming_12.md`*
