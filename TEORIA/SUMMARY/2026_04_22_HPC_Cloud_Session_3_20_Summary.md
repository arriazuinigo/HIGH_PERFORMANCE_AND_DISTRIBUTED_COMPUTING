# High Performance & Distributed Computing — Session 20: Cloud Computing — Session 3

**Date:** 2026-04-22 (Wed)
**Instructor:** Francesc Solsona Tehas (UAB)

---

## 1. Overview

This hands-on session focuses on **AWS (Amazon Web Services)** — deploying and working with a **virtual machine on AWS EC2** and running a Jupyter Notebook in the cloud.

---

## 2. Key Concepts

### 2.1 AWS Setup

- Students receive a **€50 credit** to use on AWS
- This covers several small VM instances for testing
- Session demonstrates step-by-step VM creation

### 2.2 Security Groups and Ports

To access the Jupyter Notebook on the VM:
1. Configure **Security Groups** (virtual firewall)
2. Add inbound rules for **SSH (port 22)** and **custom TCP (port 8888)** 
3. Set source to **anywhere** (0.0.0.0/0) for accessibility

**Note:** Common mistake — typing "EEC2" instead of "EC2" in the URL

### 2.3 Jupyter Notebook in the Cloud

1. Launch an EC2 instance with appropriate AMI (Amazon Machine Image)
2. SSH into the instance
3. Install Jupyter and dependencies
4. Start Jupyter Notebook server
5. Access via browser using:
   - Public IP of the instance
   - Port 8888
   - Authentication token (displayed in terminal)

**Cost:** Running a small VM for testing costs **at most ~$1.00**

---

## 3. Key Concepts Demonstrated

- **Virtual Machine** (EC2) = IaaS (Infrastructure as a Service)
- **Security Groups** control inbound/outbound traffic
- **Jupyter Notebook** running on cloud infrastructure
- File management on the VM
- Running Python code in a cloud-based notebook

---

## 4. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. AWS Setup** | 0:27–1:04 | AWS account, EC2 launch, security groups |
| **II. Live Demo** | 1:05–1:13 | Jupyter Notebook on EC2, running code |
| **III. Q&A** | 1:10–1:14 | Cost questions, further steps |
| **IV. Lab 1 Reminder** | 1:14–1:15 | Deadline May 6th for personal website |

---

## 5. Key Takeaways

- **AWS EC2** provides virtual machines (IaaS) in the cloud
- **Security groups** are essential for network access control
- Jupyter Notebook works seamlessly on cloud VMs
- Cost for small experiments is **very low** (€50 credit is sufficient)
- Lab 1 (GitHub Pages) deadline: **May 6th**

---

*Sources: Transcript `2026_04_22_Cloud. Session 3_20.md`*
