# Summary: Cloud. Session 7 (Session 27)
**Date:** May 20, 2026
**Professor:** Francesc Solsona Tehas

## Key Topics Covered

### 1. AWS Budget Management
- The professor mentioned he had spent $22.50 of his budget.
- Recommended students to **reset their labs** to avoid exceeding the budget.
- If students exceed the budget, they can email the professor to request an increase.

### 2. Client VPN Endpoint Setup
The main topic of the session was setting up a **VPN (Virtual Private Network)** to securely access AWS resources, particularly private subnets.

**Steps to create a Client VPN Endpoint:**
1. **Create the Client VPN Endpoint** in the AWS VPN service.
2. **Associate the VPN Endpoint with the VPC** — links the VPN to the Virtual Private Cloud.
3. **Authorize Rules** — configure security group rules to allow traffic from the VPN.
4. **Provide Internet Access** — configure routing so VPN-connected devices can reach the internet through the VPC.

**Configuration Files:**
- Download a configuration file from AWS.
- The file contains the structure needed for the VPN client.
- Insert the certificate and the output of specific commands into the configuration file.
- Save the file and use it with a VPN client application.

### 3. Connecting via VPN
- Download and install an OpenVPN-compatible client.
- Import the configuration file into the VPN client.
- Connect to the VPN.
- Once connected, you can SSH directly into **both public and private EC2 instances** from your local machine.
- This eliminates the need for a bastion host (jump box).

### 4. Accessing Private EC2 via VPN
- With the VPN active, SSH into the private EC2 instance using:
  - The private key (`.pem` file)
  - The private IP address of the instance
- The VPN provides a secure tunnel from your local network directly into the VPC.

### 5. Optional: File Server Example
- The professor mentioned an optional example of creating a **file server** (like Dropbox) inside a private subnet.
- This is not mandatory but available for students who want to explore further.

### 6. Course Reflection
- Students (Delia) expressed that they learned a lot about how the AWS platform works.
- The professor noted that the most important AWS knowledge has been covered in the course.
- Students can take additional AWS courses to further increase their skills.

### 7. Upcoming Assessments
- **Hole 2:** Deadline May 31.
- **Quiz 2:** Will be held on the next Wednesday (May 27).
  - Available from 12:15 until the end of the day.
  - Duration: 1 hour.
  - Students can choose when to take it within that window.
  - The professor suggested meeting in the class for the quiz.

## Key Takeaways
- VPN provides secure, direct access to private subnets without a bastion host.
- Setting up a Client VPN Endpoint involves creating the endpoint, associating it with a VPC, and configuring authorization rules.
- The VPN client configuration file requires certificates and specific command outputs.
- Quiz 2 and Hole 2 are the remaining assessments for the cloud part.
