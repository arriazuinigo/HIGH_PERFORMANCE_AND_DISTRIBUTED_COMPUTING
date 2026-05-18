# High Performance & Distributed Computing — Session 3: Complexity Analysis

**Date:** 2026-02-17 (Tue)
**Instructor:** Sandra Adriana Méndez (UAB)

---

## 1. Overview

This session introduces **algorithm complexity analysis** — describing how computation time or memory consumption grows as input size increases. This is the first topic in the Algorithmic Techniques block, led by Sandra Méndez.

---

## 2. Key Concepts

### 2.1 What is Algorithm Complexity?

- Describes how computation time or memory grows as input size increases
- **Input size** depends on domain: array dimension, number of patients, number of features, number of images, etc.
- Goal: Select algorithms with the lowest complexity for better performance

### 2.2 Linear Search vs Binary Search

| Search Type | Complexity | Requirement |
|-------------|------------|-------------|
| **Linear Search** | O(n) | No precondition |
| **Binary Search** | O(log n) | Requires sorted list |

### 2.3 Binary Search Mechanics

1. Take the middle element of the sorted list
2. Compare with the target value
3. If target > middle → search upper half
4. If target < middle → search lower half
5. Repeat until element is found (or space is exhausted)

**Complexity derivation:**
- After 1st iteration: search space = n/2
- After 2nd iteration: search space = n/4
- After k-th iteration: search space = n/2^k
- When search space = 1 → k = log₂(n)
- **Binary search = O(log n)**

### 2.4 Validating Complexity

- **Before running:** Compute theoretical complexity
- **After running:** Measure actual execution time with different input sizes
- Run multiple times to distinguish real behavior from noise
- Plot time vs input size to verify the expected growth rate

---

## 3. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. Introduction** | 0:38–2:03 | Overview of Algorithmic Techniques block |
| **II. Binary Search** | 1:04:05–1:09:18 | Detailed explanation of binary search algorithm and its O(log n) complexity |
| **III. Assignment & Closing** | 1:09:18–1:13:51 | Instructions for exercises and Q&A |

> **Note:** The transcript shows a significant gap (~1h) between the introduction and the binary search content where the main lecture content was delivered.

---

## 4. Assignments

### 4.1 Exercises

- Implement programs to compute complexity
- Validate theoretical complexity with empirical measurements
- Run tests with several input sizes
- Show graphs/plots demonstrating the observed behavior

### 4.2 Submission Format

- Submit source code + PDF explaining the solution
- Or upload a Jupyter Notebook with code + markdown explanations
- Deadline: **Two weeks** (shared with Recursive Programming assignment)

### 4.3 Grading Weight

- Algorithmic Techniques block = **35% of total grade**
- Includes assignments on: Complexity Analysis, Recursive Programming, Divide and Conquer, and Dynamic Programming

---

## 5. Key Takeaways

- Complexity helps compare algorithms before implementation
- **O(log n) is better than O(n)** — binary search over linear search
- Always **validate theoretical complexity** with empirical testing
- Run **multiple experiments** to filter out noise
- Choose algorithms with the **least complexity** for your problem domain

---

*Sources: Transcript `2026_02_17_Complexity Analysis_3.md`*
