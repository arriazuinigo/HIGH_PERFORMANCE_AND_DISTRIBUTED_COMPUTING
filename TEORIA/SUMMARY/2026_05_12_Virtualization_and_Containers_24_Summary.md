# Summary: Virtualization and Containers (Session 24)
**Date:** May 12, 2026
**Professor:** Sandra Adriana Méndez

## Key Topics Covered

### 1. Virtualization Concepts
- **Virtual Machines (VMs):** Full virtualization of both software and hardware, allowing different operating systems to run on the same physical machine.
- **Hypervisors:** Two types:
  - **Type 1 (Bare-metal):** Runs directly on hardware, common in cloud environments (servers).
  - **Type 2 (Hosted):** Runs on top of an existing OS.
- VMs virtualize the entire hardware stack (CPU, memory, network), making them heavier than containers.

### 2. Containers vs. Virtual Machines
- Containers virtualize only the software layer (OS-level virtualization), not the hardware.
- Containers are lighter, faster to start, and more efficient than VMs.
- **Docker** is the de facto standard for containers in general computing.
- **Singularity (now called Apptainer)** is the container solution designed specifically for HPC environments.

### 3. Singularity/Apptainer Commands
- **`singularity pull`**: Download an image from a registry (Docker Hub, Singularity Library, etc.).
- **`singularity run`**: Execute a container.
- **`singularity shell`**: Open an interactive shell inside the container.
- **`singularity build`**: Build a container from a definition file.
- **`singularity inspect`**: View metadata and configuration of a container image.
- **`singularity cache`**: Manage cached images (list, clean).
- **`singularity rm`**: Remove container images.

### 4. Definition Files
- Equivalent to Dockerfiles for Singularity containers.
- Contain all information needed to reproduce a container: header, post-section (installed packages), environment variables, and run commands.
- Essential for reproducibility in HPC workflows.

### 5. Image Sources
- **Docker Hub**: `singularity pull docker://<image>`
- **Singularity Library**: `singularity pull library://<image>`
- **Sylabs Cloud Builder**: Online service to build containers.

### 6. HPC Context
- Singularity is preferred in HPC because it integrates better with cluster schedulers (SLURM) and does not require root privileges.
- Containers in HPC allow reproducible research and easy software deployment.

### 7. Final Assignment Information
- The professor announced a final assignment combining: dynamic programming, workflow management (Make/Snakemake), Singularity containers, and regular expressions.
- Originally planned for 2 days (May 26-27), but due to student requests, it was moved to after the summer school (around June 12-14).
- The assignment is designed to test understanding of all the last topics covered.

## Key Takeaways
- Containers are more lightweight than VMs because they share the host OS kernel.
- Docker is for general use; Singularity/Apptainer is for HPC.
- Definition files are crucial for container reproducibility.
- The final assignment will integrate multiple course topics.
