# High Performance & Distributed Computing — Session 21: Virtualization and Environments

**Date:** 2026-04-28 (Wed)
**Instructor:** Sandra Adriana Méndez (UAB)

---

## 1. Overview

This session covers **Conda environments** and the motivation for **reproducibility** through environment and container management. It focuses on creating isolated Python environments to manage dependencies and share reproducible computational setups.

---

## 2. Key Concepts

### 2.1 The Reproducibility Problem

- Research experiments are **difficult to reproduce**
- A 2016 study found most scientific results cannot be independently verified
- **Causes:** Different software versions, dependency conflicts, OS differences

### 2.2 Conda Virtual Environments

| Command | Purpose |
|---------|---------|
| `conda create --name myenv` | Create a new environment |
| `conda activate myenv` | Activate an environment |
| `conda deactivate` | Deactivate current environment |
| `conda install package_name` | Install package in active env |
| `conda env export > environment.yml` | Export environment description |
| `conda env create -f environment.yml` | Recreate environment from file |
| `conda env remove --name myenv` | Remove environment |

### 2.3 Key Benefits

| Benefit | Description |
|---------|-------------|
| **Isolation** | Each environment has its own packages and dependencies |
| **Dependency management** | Avoid conflicts between projects |
| **Reproducibility** | Share `environment.yml` to recreate exact setup |
| **No admin rights needed** | Install packages without sudo (important on clusters) |

### 2.4 Important: Space Management

- Environments consume disk space (check with `du -sh`)
- On shared clusters, **monitor space usage**
- Remove unused environments (`conda env remove`)
- The working directory and environment directory are **separate**

### 2.5 From Environments to Containers

- **Conda** solves dependency management at the software/library level
- **Containers (Docker/Singularity)** solve the OS-level reproducibility
- Containers include the operating system + software → **true reproducibility**

| Approach | Scope | Portability |
|----------|-------|-------------|
| **Conda environment** | Python packages | Same OS family |
| **Container** | OS + all software | Any system (Linux, HPC, Cloud) |

---

## 3. Recommendation

1. **Connect to the cluster**
2. **Create a Conda environment**
3. **Install packages and test**
4. **Export the environment** to a YAML file
5. **Recreate it** in another location
6. **Remove it** when no longer needed

---

## 4. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. Introduction** | 0:13–1:06 | Reproducibility problem, why environments |
| **II. Conda Demo** | 38:55–43:50 | Live demo on cluster: create, activate, install, export, remove |
| **III. Containers Preview** | 45:12–46:57 | Conda vs containers, true reproducibility |
| **IV. Closing** | 46:57–47:49 | Practice recommendations |

---

## 5. Key Takeaways

- **Conda environments** isolate project dependencies
- **`environment.yml`** enables sharing and reproducibility
- Environments can be created **without admin permissions**
- **Monitor disk space** on shared systems
- **Containers** go further by including the OS for true reproducibility

---

*Sources: Transcript `2026_04_28_Virtualization and Environments_21.md`*
