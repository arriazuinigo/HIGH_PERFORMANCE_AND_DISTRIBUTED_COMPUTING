# Summary: Cloud. Session 6 (Session 25)
**Date:** May 13, 2026
**Professor:** Francesc Solsona Tehas

## Key Topics Covered

### 1. AWS Networking Concepts
- **Public vs. Private IP Addresses:**
  - Public IPs are accessible from the internet.
  - Private IPs are only accessible within the VPC.
  - Every time a lab is restarted, the public IP changes (dynamic IP allocation).
- **DNS Names vs. Public IPs:** Both can be used to connect to an instance.

### 2. Internet Gateway (IGW)
- An Internet Gateway is required to allow traffic between a VPC and the internet.
- **Steps to attach an IGW to a VPC:**
  1. Create the Internet Gateway.
  2. Attach it to the desired VPC.
  3. Create a Route Table.
  4. Add a route with destination `0.0.0.0/0` (all internet traffic) pointing to the IGW.
  5. Associate the Route Table with the public subnet.

### 3. Route Tables
- Define how network traffic is directed within a VPC.
- A route to `0.0.0.0/0` via the Internet Gateway makes a subnet public.
- Without this route, the subnet remains private (no internet access).

### 4. Launching EC2 Instances in Public vs. Private Subnets
- **Public Subnet EC2:** Accessible from the internet via its public IP/DNS.
- **Private Subnet EC2:** Not directly accessible from the internet; has no public IP.

### 5. Accessing a Private EC2 Instance (Bastion/Jump Host)
- To access a private EC2 instance:
  1. Copy the private key (`.pem` file) to the public EC2 instance.
  2. SSH into the public instance.
  3. From the public instance, SSH into the private instance using its **private IP address**.
- This method uses the public instance as a **bastion host** or **jump box**.

### 6. Key Practical Steps Demonstrated
- Creating and attaching an Internet Gateway to a VPC.
- Creating Route Tables and associating them with subnets.
- Launching EC2 instances in both public and private subnets.
- Copying SSH keys between instances using `scp`.
- Connecting from a public instance to a private instance via SSH.

## Key Takeaways
- Internet Gateway + Route Table = Public subnet (internet accessible).
- Private subnets have no direct internet access.
- Bastion hosts (public EC2) are used to access private EC2 instances.
- Private instances use private IPs for internal communication.
