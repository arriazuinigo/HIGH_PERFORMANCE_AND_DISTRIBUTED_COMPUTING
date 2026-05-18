# High Performance & Distributed Computing — Session 2: Linux Processes

**Date:** 2026-02-11 (Wed) · **Duration:** ~1h 0m
**Instructor:** Miquel Àngel Senar Rosell (UAB)

---

## 1. Overview

This session covers the fundamentals of **Linux processes** and how to exploit **parallel computing** on a single multi-core machine. The core idea is that modern computers have multi-core processors, enabling us to run multiple applications simultaneously — the foundation of parallel computing.

---

## 2. Key Concepts

### 2.1 Parallel Computing Motivation

- Modern computers have multi-core processors → capacity to run multiple applications at the same time
- Problem decomposition: divide problems into independent pieces that can be computed separately
- Goal: Reduce total execution time by using available computing resources

### 2.2 Foreground vs Background Processes

| Concept | Description |
|---------|-------------|
| **Foreground (synchronous)** | Process tied to terminal; terminal is blocked until process finishes |
| **Background (asynchronous)** | Process runs without direct terminal connection; terminal remains free |
| **`&` (ampersand)** | Appended to command to run process in background |

### 2.3 Process Management Commands

| Command | Purpose |
|---------|---------|
| `ps` | List running processes with IDs, execution time, and commands |
| `kill -9 <PID>` | Forcefully terminate a process |
| `kill -STOP <PID>` | Pause a process |
| `kill -CONT <PID>` | Resume a paused process |
| `jobs` | List background jobs |
| `fg` | Move a background job to foreground |
| `bg` | Move a foreground job to background |

### 2.4 Practical Example: Counting Primes

- A `count_primes` program counts primes in a given interval
- Running multiple instances with `&` uses multiple cores simultaneously
- Example: Launch 3 instances → each uses ~1 core → 3 cores exploited

### 2.5 Output Behavior of Background Processes

- **Question from student** (Michael Eskander): How to see results of background processes?
- **Answer:** Output appears on the terminal as it's produced, but without any order or formatting control — may interleave with user typing

---

## 3. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. Introduction** | 0:03–2:19 | Parallel computing concepts, multi-core processors |
| **II. Main Content** | 2:19–55:27 | Foreground/background, `ps`, `kill`, `jobs`, ampersand usage |
| **III. Q&A** | 55:39–56:34 | Student question on background process output |
| **IV. Closing & Exercise** | 56:36–59:23 | Informal homework assignment |

---

## 4. Homework / Exercise

1. Connect to the cluster
2. Download the `count_primes` program (to be published on Moodle)
3. Practice running it with the ampersand (`&`) mechanism
4. Experiment with foreground/background commands (`jobs`, `fg`, `bg`)
5. Practice process control (`kill`, `kill -STOP`, `kill -CONT`)
6. Practice file transfer: copy files to/from the cluster

> **Note:** This is an informal exercise to prepare for parallel application execution on the cluster.

---

## 5. Key Takeaways

- **Ampersand (`&`)** is the simplest way to run parallel processes on a single machine
- Background processes free the terminal for further commands
- Process IDs (PIDs) are used to identify and control running processes
- The OS manages background process execution across available cores
- Running multiple independent instances = coarse-grained parallelism without special programming

---

*Sources: Transcript `2026_02_11_Linux Processes_2.md`*
