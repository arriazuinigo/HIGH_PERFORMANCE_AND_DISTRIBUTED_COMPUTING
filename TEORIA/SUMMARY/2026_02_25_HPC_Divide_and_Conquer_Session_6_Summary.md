# High Performance & Distributed Computing — Session 6: Divide and Conquer

**Date:** 2026-02-25 (Wed)
**Instructor:** Sandra Adriana Méndez (UAB)

---

## 1. Overview

This session introduces the **Divide and Conquer** algorithmic paradigm. The core idea: break a large problem into smaller subproblems, solve them recursively, and combine the solutions to obtain the final result.

---

## 2. Key Concepts

### 2.1 What is Divide and Conquer?

1. **Divide:** Split the big problem into smaller, manageable subproblems
2. **Conquer:** Solve each subproblem (recursively or directly)
3. **Combine:** Merge subproblem solutions into the final solution

**Main benefit:** Reduces the problem space, making complex problems tractable.

### 2.2 Algorithms Covered

#### Linear Search — O(n)
- Iterates over the entire list comparing each element
- No precondition required
- Simple but inefficient for large datasets

#### Binary Search — O(log n)
- Requires a **sorted list** as precondition
- Divides search space in half each step
- Efficient but data must be pre-sorted

#### Merge Sort — O(n log n)
- Follows the divide-and-conquer approach
- Recursively splits array into halves, sorts each, then merges
- **Stable** sorting algorithm
- Complexity: O(n log n) time, O(n) auxiliary space

### 2.3 Why Understanding Sorting Matters

- Many algorithms (like binary search) require **sorted data**
- Different sorting algorithms have different complexities
- Python provides built-in sorting functions, but understanding their underlying behavior and complexity helps with algorithm selection

---

## 3. Q&A Highlights

**Question from Celica Krigul:** Can we just use Python's built-in `sort()` function?

**Sandra's response:**
- Yes, Python provides optimized sorting functions
- The course goal is to **understand what happens behind the scenes**
- Knowing complexity helps you **select the right algorithm** for your data size
- Built-in libraries are convenient, but choosing the wrong algorithm leads to performance issues with large data
- The emphasis is on **understanding complexity** rather than reimplementing everything

---

## 4. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. Introduction** | 0:03–2:28 | Divide and conquer concept definition |
| **II. Searching Algorithms** | 2:28–2:47 | Linear search review |
| **III. Binary Search & Merge Sort** | 41:18–44:27 | Detailed walkthrough of both algorithms |
| **IV. Q&A** | 44:27–50:08 | Student questions on built-in functions |
| **V. Closing** | 50:08–52:07 | Assignment reminders and next steps |

---

## 5. Assignments Status

- **Complexity Analysis and Recursion** assignments are still open
- Divide and Conquer assignment will be released **after current assignments are completed**
- Students are advised to finish current work before new material is added

---

## 6. Key Takeaways

- **Divide and Conquer** reduces problem complexity by recursive subdivision
- **Merge Sort** (O(n log n)) is a classic example of this paradigm
- Understanding **underlying algorithms** helps choose the right tool
- Python libraries are convenient, but complexity awareness is crucial for scaling
- Always consider whether your data needs **sorting** as a preprocessing step

---

*Sources: Transcript `2026_02_25_Divide and Conquer_6.md`*
