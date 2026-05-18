# High Performance & Distributed Computing — Session 4: Recursive Programming

**Date:** 2026-02-18 (Wed)
**Instructor:** Sandra Adriana Méndez (UAB)

---

## 1. Overview

This session covers **recursive programming**, the second topic in the Algorithmic Techniques block. Recursion is a technique where a function calls itself to break down a problem into similar subproblems.

---

## 2. Key Concepts

### 2.1 What is Recursion?

- A function that calls itself (directly or indirectly)
- Technique to break a problem into one or more **similar subproblems**
- Each subproblem is a smaller instance of the original problem
- Two components: **base case** and **recursive case**

### 2.2 Recursion vs Iteration

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| **Memory usage** | Higher (each call adds stack frame) | Lower |
| **Naturalness** | More natural for certain problems | More natural for others |
| **Time complexity** | Can be same or different | Can be same or different |
| **Readability** | Often more readable for divide-and-conquer | More readable for simple loops |

### 2.3 Complexity Considerations

- **Recursive does NOT automatically mean exponential complexity**
- Need to analyze:
  - **Number of recursive calls** → time complexity
  - **Depth of recursion** → space complexity (stack frames in memory)
- **Divide by 2** (e.g., binary search) → logarithmic complexity
- **Two or more recursive branches** → potentially exponential complexity

### 2.4 Examples Covered

| Example | Complexity | Notes |
|---------|------------|-------|
| **Fibonacci (naive)** | O(2ⁿ) exponential | Duplicate work; multiple recursive branches |
| **Binary search** | O(log n) logarithmic | Reduces search space by half each step |

### 2.5 Space Complexity

- Important when memory is restricted
- Each recursive call requires stack memory
- Deep recursion may cause **stack overflow**
- Iterative version may be preferred when memory is constrained

---

## 3. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. Introduction** | 0:32–2:00 | Presentation mode setup; definition of recursion |
| **II. Main Content** | 2:00–45:46 | Recursion concepts, complexity analysis, Fibonacci examples |
| **III. Q&A & Closing** | 45:46–50:16 | Assignment details and questions |

---

## 4. Assignments

### 4.1 Recursive Programming Exercises

- Implement recursive functions for **3 problems** provided
- Compute and report the **time complexity** of each solution
- Validate with **empirical measurements** (vary input size, measure time)
- Analyze any **space complexity** issues

### 4.2 Submission Requirements

- Submit **source code** (Python files or Jupyter Notebook)
- Include **PDF explanation** or markdown cells with analysis
- Deadline: **2 weeks** (combined with Complexity Analysis exercises)

---

## 5. Key Takeaways

- Recursion = function calling itself to solve subproblems
- Complexity analysis is crucial — recursion ≠ exponential
- **Divide input by 2** → likely O(log n); **multiple branches** → potentially exponential
- **Space complexity** matters: each call consumes stack memory
- Always validate complexity with **experimental measurements**

---

*Sources: Transcript `2026_02_18_Recursive Programming_4.md`*
