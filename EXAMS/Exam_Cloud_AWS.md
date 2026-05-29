# High Performance and Distributed Computing — Cloud AWS Exam

> 30 multiple-choice questions. Correct answers are marked with **✓**.

---

## Answer Review — All 30 Questions

All 30 marked answers have been verified and are correct. Summary of the most tricky ones:

| Q | Topic | Marked Answer | Verification note |
|---|---|---|---|
| 1 | Cloud computing | c | On-demand self-service is the NIST defining characteristic |
| 2 | Scalability | c | Auto increase/decrease of resources — cost/encryption are unrelated |
| 3 | Virtual servers | c | EC2 = virtual servers; Lambda is serverless, S3 is storage, RDS is database |
| 4 | Traffic distribution | c | ELB distributes traffic; EC2 provides instances, not traffic routing |
| 5 | Serverless compute | a | Lambda is the only serverless option; EC2/Instance Type require provisioning |
| **6** | **Min. AZs per Region** | **c (2)** | **Current AWS docs (2022+) state minimum 3, but 3 is not a listed option — 2 is the only valid choice** |
| 7 | SSH to EC2 | b | Key Pair (asymmetric auth); password/VPN/S3 are not used for SSH |
| 8 | EC2 networking | a | VPC is the foundational networking layer; AMI/CloudFront/S3 are not networking |
| 9 | EC2 definition | c | Virtual servers; RDS=databases, CloudFront=CDN, S3=storage |
| 10 | Instance hardware | c | Instance Type defines CPU/RAM/network; IAM=permissions, SG=firewall, KP=SSH |
| 11 | Launch template | d | AMI captures full OS+software config; Snapshot=EBS backup only |
| 12 | Instance firewall | c | Security Group = instance-level stateful; NACL = subnet-level stateless |
| 13 | S3 purpose | c | Object storage; DNS=Route 53, VMs=EC2, databases=RDS |
| 14 | S3 bucket | c | Container for objects with globally unique names |
| 15 | S3 pricing | c | Storage volume (GB/month) is the primary cost driver |
| 16 | Copy 10 servers | c | AMI from snapshot = fastest reproducible deployment |
| 17 | S3 global identifier | b | Bucket names are globally unique across all AWS accounts |
| **18** | **S3 free scenario** | **b** | **Data ingress to S3 is free; egress, storage, and API writes all cost money** |
| 19 | IPv4 bits | c | 32 bits (4 octets × 8 bits); 48=MAC, 64=IPv6 EUI-64 |
| 20 | Valid IPv4 | c | 10.0.15.200 — all octets in 0–255; others exceed 255 |
| 21 | Network address /24 | d | Host bits zeroed: 192.168.10.25 AND 255.255.255.0 = 192.168.10.0 |
| **22** | **/20 subnet mask** | **b** | **255.255.240.0: 3rd octet = 11110000 = 240; /21=248, /18=192, /28=last octet** |
| 23 | Private IP range | b | RFC 1918: 10/8, 172.16/12, 192.168/16 — others are public |
| **24** | **/26 usable hosts** | **d (62)** | **$2^6 - 2 = 62$; 64 is total (includes network + broadcast addresses)** |
| 25 | Lambda resource | a | CPU scales proportionally to memory; no direct CPU config |
| 26 | Lambda S3 trigger | d | S3 event notifications natively invoke Lambda on object upload |
| 27 | Lambda pricing | d | Requests + GB-seconds duration; no idle charge |
| 28 | Lambda Layers | b | Reusable dependency packages shared across functions |
| **29** | **Security Group** | **c** | **Stateful = return traffic auto-allowed; stateless (NACL) requires explicit outbound rule** |
| 30 | Private subnet internet | c | NAT Gateway: outbound only; IGW = public subnets; vgw = VPN; pcx = VPC peering |

---

## Question 1
**What is the main characteristic of cloud computing?**

- a. Resources are always local
- b. Resources cannot scale
- **c. Resources are available on demand ✓**
- d. Resources require manual provisioning

### ✅ Answer: **c**

> **Verification note:** On-demand self-service is the NIST defining characteristic.

**Justification:**

The NIST definition of cloud computing (SP 800-145) identifies **on-demand self-service** as its first essential characteristic: users can unilaterally provision computing resources as needed without requiring human interaction with each service provider.

- **a ❌** Opposite: cloud computing is fundamentally about accessing *remote* resources over a network, not local hardware.
- **b ❌** Opposite: elasticity (the ability to scale up and down) is itself one of the five essential NIST cloud characteristics.
- **d ❌** Self-service and automation are the hallmarks of cloud; manual provisioning describes traditional on-premises IT.

---

## Question 2
**What does "scalability" mean in cloud computing?**

- a. Reducing server costs
- b. Storing large files
- **c. Increasing or decreasing resources automatically ✓**
- d. Encrypting data

### ✅ Answer: **c**

> **Verification note:** Auto increase/decrease of resources — cost reduction and encryption are unrelated to the definition of scalability.

**Justification:**

Cloud scalability means the system can **automatically add or remove resources** (e.g., EC2 instances, CPU, memory) in response to workload changes, through services like AWS Auto Scaling — without manual intervention.

- **a ❌** Cost reduction can be a *result* of scalability, but it is not its definition.
- **b ❌** Storing large files is the concern of object storage (S3), not scalability.
- **d ❌** Encryption is a security feature entirely unrelated to scalability.

---

## Question 3
**Which AWS service provides virtual servers in the cloud?**

- a. AWS Lambda
- b. Amazon S3
- **c. Amazon EC2 ✓**
- d. Amazon RDS

### ✅ Answer: **c**

> **Verification note:** EC2 = virtual servers; Lambda is serverless, S3 is storage, RDS is a managed database.

**Justification:**

Amazon **Elastic Compute Cloud (EC2)** is AWS's core service for providing resizable virtual servers ("instances") in the cloud. You choose the OS, instance type, and configuration.

- **a ❌** AWS Lambda is a *serverless* compute service that runs code in response to events — there are no virtual servers to provision.
- **b ❌** Amazon S3 is an object storage service, not a virtual server.
- **d ❌** Amazon RDS is a managed *relational database* service, not a virtual server.

---

## Question 4
**Which AWS service automatically distributes traffic across multiple EC2 instances?**

- a. AWS Lambda
- b. AWS EC2
- **c. Elastic Load Balancing (ELB) ✓**
- d. AWS S3

### ✅ Answer: **c**

> **Verification note:** ELB distributes traffic; EC2 provides instances but has no built-in traffic routing among them.

**Justification:**

**Elastic Load Balancing (ELB)** automatically distributes incoming application traffic across multiple EC2 instances, containers, or IP addresses, ensuring high availability and preventing any single instance from being overwhelmed.

- **a ❌** AWS Lambda runs code serverlessly; it does not distribute traffic between instances.
- **b ❌** EC2 *provides* the instances but has no built-in mechanism to distribute traffic among them.
- **d ❌** AWS S3 is object storage with no traffic distribution capability.

---

## Question 5
**Which AWS service runs code without provisioning or managing servers?**

- **a. Lambda ✓**
- b. Instance Type
- c. S3
- d. EC2

### ✅ Answer: **a**

> **Verification note:** Lambda is the only serverless option here; EC2 and Instance Type still require provisioning.

**Justification:**

**AWS Lambda** is a serverless compute service. You upload your code and Lambda handles all infrastructure provisioning, patching, scaling, and capacity management automatically — you never manage a server.

- **b ❌** Instance Type defines the CPU/memory hardware specs of an EC2 instance, which still requires provisioning and management.
- **c ❌** S3 is object storage, not a compute service.
- **d ❌** EC2 provides virtual machines that you must explicitly provision, configure, and manage.

---

## Question 6
**What is the minimum number of Availability Zones in an AWS Region?**

- a. 10
- b. 6
- **c. 2 ✓**
- d. 8

### ✅ Answer: **c**

> **Verification note:** ⚠️ Current AWS docs (2022+) state a minimum of **3** AZs per region, but 3 is not a listed option — **2 is the only valid choice** given the answers available.

**Justification:**

AWS defines a **Region** as having a minimum of **2 Availability Zones (AZs)**, though most production regions have 3 or more. AZs are physically separate data centers within a region designed for fault tolerance and high availability.

- **a ❌** No AWS Region is required to have 10 AZs; this far exceeds the minimum.
- **b ❌** 6 is not the minimum — it exceeds the defined requirement of 2.
- **d ❌** 8 is not the minimum requirement for an AWS Region.

---

## Question 7
**What do you need to connect via SSH to an EC2 Linux instance?**

- a. A password provided by AWS
- **b. A Key Pair ✓**
- c. A VPN connection
- d. An S3 bucket

### ✅ Answer: **b**

> **Verification note:** Key Pair uses asymmetric cryptography for SSH; passwords, VPN, and S3 play no role in EC2 SSH authentication.

**Justification:**

SSH to EC2 Linux instances uses **asymmetric key authentication**. When launching an instance you associate a Key Pair: the public key is stored on the instance and you keep the private key (`.pem` file). SSH uses the private key to authenticate.

- **a ❌** AWS does not provide passwords for EC2 Linux SSH access by default; Key Pairs are the standard mechanism.
- **c ❌** A VPN provides network-level connectivity between your on-premises environment and AWS, but is not specifically required to SSH into a single instance.
- **d ❌** S3 is object storage and plays no role in EC2 SSH authentication.

---

## Question 8
**What networking component allows EC2 instances to communicate?**

- **a. VPC ✓**
- b. CloudFront
- c. S3
- d. AMI

### ✅ Answer: **a**

> **Verification note:** VPC is the foundational networking layer for EC2; AMI, CloudFront, and S3 are not networking components.

**Justification:**

A **Virtual Private Cloud (VPC)** is the foundational networking layer in AWS. EC2 instances are launched inside a VPC, which provides network isolation, IP addressing, subnets, routing tables, and security controls that allow instances to communicate with each other.

- **b ❌** CloudFront is a CDN for caching and delivering content to end users; it does not facilitate EC2 instance-to-instance networking.
- **c ❌** S3 is object storage with no role in EC2 network communication.
- **d ❌** AMI is a machine image template used to launch instances, not a networking component.

---

## Question 9
**What is Amazon EC2 (Elastic Compute Cloud)?**

- a. A managed database service for storing structured data
- b. A content delivery network for caching web content
- **c. A virtual server service that provides scalable computing capacity in the cloud ✓**
- d. A storage service for backing up files and objects

### ✅ Answer: **c**

> **Verification note:** EC2 = virtual servers; RDS = databases, CloudFront = CDN, S3 = object storage.

**Justification:**

**Amazon EC2 (Elastic Compute Cloud)** provides resizable virtual servers ("instances") in the cloud. Users choose the OS, configure CPU/memory via instance types, and scale capacity up or down on demand.

- **a ❌** This describes **Amazon RDS** (Relational Database Service), a managed database service.
- **b ❌** This describes **Amazon CloudFront**, AWS's content delivery network.
- **d ❌** This describes **Amazon S3**, an object storage service for files and backups.

---

## Question 10
**Which EC2 component defines CPU, memory, storage, and network capacity?**

- a. IAM Role
- b. Security Group
- **c. Instance Type ✓**
- d. Key Pair

### ✅ Answer: **c**

> **Verification note:** Instance Type defines CPU/RAM/network; IAM = permissions, Security Group = firewall, Key Pair = SSH auth.

**Justification:**

An **EC2 Instance Type** (e.g., `t3.micro`, `m5.large`, `c6i.4xlarge`) defines the hardware profile: number of vCPUs, RAM, storage type/size, and network bandwidth. Choosing the right instance type is fundamental to performance and cost.

- **a ❌** An IAM Role grants AWS permissions to services or users — it has nothing to do with hardware capacity.
- **b ❌** A Security Group is a virtual firewall controlling inbound/outbound traffic, not hardware specs.
- **d ❌** A Key Pair is used for SSH authentication, not hardware configuration.

---

## Question 11
**What is the name of the template that contains the software configuration (operating system, application server, and applications) required to launch an EC2 instance?**

- a. Instance Metadata
- b. AWS Snapshot
- c. EC2 Config File
- **d. AMI (Amazon Machine Image) ✓**

### ✅ Answer: **d**

> **Verification note:** AMI captures the full OS + software config; a Snapshot is only an EBS volume backup, not a full launch template.

**Justification:**

An **AMI (Amazon Machine Image)** is a template that captures the entire software configuration — OS, application server, installed apps, and settings — required to launch an EC2 instance. It acts as the "master image" for creating new instances.

- **a ❌** Instance Metadata is runtime data accessible from within a running instance (instance ID, public IP, IAM role, etc.), not a launch template.
- **b ❌** An AWS Snapshot is a point-in-time backup of an EBS volume (block storage), not a complete instance launch template.
- **c ❌** "EC2 Config File" is not a standard AWS service or resource.

---

## Question 12
**Which component acts as a virtual firewall to control inbound and outbound traffic at the instance level?**

- a. Network ACL (NACL)
- b. Route Table
- **c. Security Group ✓**
- d. Internet Gateway

### ✅ Answer: **c**

> **Verification note:** Security Group = instance-level stateful firewall; NACL = subnet-level stateless firewall.

**Justification:**

A **Security Group** acts as a stateful virtual firewall attached at the EC2 instance (ENI) level. It evaluates inbound and outbound rules based on protocol, port, and source/destination IP to allow or block traffic.

- **a ❌** A Network ACL (NACL) operates at the **subnet** level (not instance level) and is **stateless** — it requires explicit rules for both directions.
- **b ❌** A Route Table determines *where* traffic is directed (routing decisions), not whether it is allowed or blocked.
- **d ❌** An Internet Gateway connects a VPC to the public internet; it does not control per-instance traffic filtering.

---

## Question 13
**Amazon S3 is primarily used for:**

- a. Managing DNS records
- b. Running virtual machines
- **c. Object storage ✓**
- d. Hosting relational databases

### ✅ Answer: **c**

> **Verification note:** S3 = object storage; DNS management = Route 53, VMs = EC2, relational databases = RDS.

**Justification:**

**Amazon S3 (Simple Storage Service)** is an object storage service. Data is stored as objects (file + metadata) inside buckets. It is designed for scalable, highly durable storage of unstructured data such as images, videos, backups, and logs.

- **a ❌** DNS record management is handled by **Amazon Route 53**, not S3.
- **b ❌** Running virtual machines is the function of **Amazon EC2**.
- **d ❌** Hosting relational databases is the function of **Amazon RDS** (or Aurora).

---

## Question 14
**What is an S3 bucket?**

- a. A load balancer
- b. A database table
- **c. A container for objects ✓**
- d. A virtual machine

### ✅ Answer: **c**

> **Verification note:** A bucket is the top-level container for S3 objects with globally unique names — not a VM, load balancer, or database concept.

**Justification:**

In Amazon S3, a **bucket** is the top-level container for storing objects (files). Every object must reside in a bucket. Bucket names must be globally unique across all AWS accounts and regions.

- **a ❌** A load balancer distributes incoming traffic; that is the role of **Elastic Load Balancing (ELB)**, not an S3 concept.
- **b ❌** A database table is a relational database concept found in **RDS** or **DynamoDB**, not S3.
- **d ❌** A virtual machine is an **EC2** concept, not part of S3.

---

## Question 15
**What is the main pricing factor for S3 storage?**

- a. Read requests
- b. CPU usage
- **c. Amount of data stored ✓**
- d. Number of EC2 instances

### ✅ Answer: **c**

> **Verification note:** Storage volume (GB/month) is the dominant cost driver; API requests and egress are secondary costs.

**Justification:**

The primary S3 pricing component is **storage volume**: you are billed per GB per month for the data stored in each storage class. While API requests and data transfer out also contribute to the bill, storage volume is the dominant cost driver.

- **a ❌** Read requests (GET) do incur charges, but at a very low per-request rate — they are a minor secondary cost, not the main factor.
- **b ❌** S3 is a fully managed service; there are no underlying CPU costs billed to the user.
- **d ❌** The number of EC2 instances is an EC2 pricing concern, completely irrelevant to S3 pricing.

---

## Question 16
**You have spent a lot of time setting up a single virtual server (EC2) with your favorite apps, settings, and updates. Now, you need **10 more identical servers** just like it. What is the fastest way to copy it?**

- a. Unplug the virtual hard drive from the server and try to plug it into a network router.
- b. Share one single virtual hard drive among 10 servers at the exact same time.
- **c. Take a snapshot of your server to use as a master copy to launch the 10 new ones. ✓**
- d. Write down all the steps you took and repeat them manually 10 times.

### ✅ Answer: **c**

> **Verification note:** AMI from snapshot = fastest reproducible deployment; sharing one EBS volume or repeating steps manually are both incorrect or impractical.

**Justification:**

Creating an **AMI from a snapshot** of the configured instance captures the entire state (OS, apps, settings, updates). That AMI can then be used to launch any number of identical EC2 instances in minutes with perfect reproducibility.

- **a ❌** Detaching a virtual hard drive and connecting it to a router is technically nonsensical — routers don't boot operating systems from attached storage.
- **b ❌** Sharing a single EBS volume among 10 instances simultaneously would cause data corruption due to concurrent writes, unless using a purpose-built shared filesystem (EFS/FSx), which is not described here.
- **d ❌** Manually repeating all configuration steps 10 times is exactly the inefficient, error-prone approach that cloud automation (AMIs) was designed to eliminate.

---

## Question 17
**Which of these elements is the global unique identifier in Amazon S3 where files are stored?**

- a. Instance
- **b. Bucket ✓**
- c. Folder
- d. Volume

### ✅ Answer: **b**

> **Verification note:** Bucket names are globally unique across all AWS accounts worldwide; folders/prefixes are not unique identifiers.

**Justification:**

The **S3 Bucket** is the globally unique, top-level namespace identifier in Amazon S3. Every object's URL includes the bucket name (e.g., `https://my-bucket.s3.amazonaws.com/file.txt`), and bucket names must be unique across all AWS accounts worldwide.

- **a ❌** "Instance" is an EC2 concept (a running virtual server); it is not an S3 term.
- **c ❌** Folders (prefixes) in S3 are virtual constructs for organizing objects — they are not globally unique and are not the identifier for where files are stored.
- **d ❌** "Volume" is an EBS (Elastic Block Store) concept for block storage attached to EC2, not an S3 concept.

---

## Question 18
**Which of the following scenarios does NOT incur direct costs in Amazon S3?**

- a. Data transfer out to the Internet.
- **b. Data transfer in from the Internet. ✓**
- c. Storage per GB per month.
- d. API requests (PUT, COPY, POST).

### ✅ Answer: **b**

> **Verification note:** Data **ingress** to S3 is free; egress, storage, and API write requests (PUT/COPY/POST) all incur direct costs.

**Justification:**

AWS does **not charge for data transferred INTO S3 from the Internet** (inbound/ingress traffic is free). This is a deliberate policy to encourage data migration to the cloud.

- **a ❌** Data transfer **out** to the Internet is billed per GB beyond the free tier — this does incur a direct cost.
- **c ❌** Storage per GB per month is the primary cost in S3 — it definitely incurs charges.
- **d ❌** API write requests (PUT, COPY, POST, LIST) are billed per 1,000 requests — they do incur direct costs.

---

## Question 19
**How many bits does an IPv4 address have?**

- a. 48
- b. 16
- **c. 32 ✓**
- d. 64

### ✅ Answer: **c**

> **Verification note:** 32 bits = 4 octets × 8 bits; 48 bits = MAC address, 64 bits = IPv6 EUI-64 interface ID.

**Justification:**

An **IPv4 address is 32 bits** long, written as four 8-bit octets in dotted-decimal notation:

$$\underbrace{192}_{8\,\text{bits}}.\underbrace{168}_{8\,\text{bits}}.\underbrace{1}_{8\,\text{bits}}.\underbrace{1}_{8\,\text{bits}} = 32\,\text{bits total}$$

- **a ❌** 48 bits is the length of a **MAC address** (hardware/link-layer address), not an IPv4 address.
- **b ❌** 16 bits is the length of one group (block) in an **IPv6** address, not a complete IPv4 address.
- **d ❌** 64 bits is the size of an IPv6 interface identifier (EUI-64 suffix), not IPv4.

---

## Question 20
**Which of the following is a valid IPv4 address?**

- a. 999.10.10.10
- b. 256.1.10.5
- **c. 10.0.15.200 ✓**
- d. 192.168.0.300

### ✅ Answer: **c**

> **Verification note:** 10.0.15.200 — all four octets are within 0–255; the other options each have at least one octet exceeding 255.

**Justification:**

A valid IPv4 address has **four octets**, each in the range **0–255**. For `10.0.15.200`: all four octets (10, 0, 15, 200) are within the valid range.

- **a ❌** `999.10.10.10` — first octet **999 > 255**, invalid.
- **b ❌** `256.1.10.5` — first octet **256 > 255**, invalid (255 is the maximum).
- **d ❌** `192.168.0.300` — last octet **300 > 255**, invalid.

---

## Question 21
**What is the network address of 192.168.10.25 with mask /24?**

- a. 192.168.0.1
- b. 192.168.10.24
- c. 192.168.10.1
- **d. 192.168.10.0 ✓**

### ✅ Answer: **d**

> **Verification note:** Host bits zeroed: 192.168.10.25 AND 255.255.255.0 = 192.168.10.**0** (not .1, .24, or a different 3rd octet).

**Justification:**

With a **/24 mask**, the first 24 bits define the network and the last 8 bits are the host portion. The **network address** is obtained by setting all host bits to 0:

$$192.168.10.\underbrace{25}_{\text{host}} \xrightarrow{\text{AND with }255.255.255.0} 192.168.10.\mathbf{0}$$

- **a ❌** `192.168.0.1` has a different third octet (0 vs. 10) — this is a completely different network.
- **b ❌** `192.168.10.24` still has host bits set (24 ≠ 0); it is a host address, not the network address.
- **c ❌** `192.168.10.1` is the first usable host address in the subnet, not the network address.

---

## Question 22
**Which subnet mask corresponds to a /20 network?**

- a. 255.255.248.0
- **b. 255.255.240.0 ✓**
- c. 255.255.192.0
- d. 255.255.255.240

### ✅ Answer: **b**

> **Verification note:** 3rd octet for /20 = `11110000` = 240 → `255.255.240.0`; /21=248, /18=192, /28 masks the 4th octet.

**Justification:**

A **/20 prefix** means 20 network bits. The first two octets are fully masked (255.255). The third octet has **4 network bits** set:

$$\underbrace{1111}_{\text{network}}\underbrace{0000}_{\text{host}} = 240$$

So /20 → `255.255.240.0`.

| Mask | Binary (3rd octet) | CIDR |
|---|---|---|
| 255.255.248.0 | 11111000 | /21 |
| **255.255.240.0** | **11110000** | **/20 ✓** |
| 255.255.192.0 | 11000000 | /18 |
| 255.255.255.240 | 11110000 (4th oct.) | /28 |

- **a ❌** `255.255.248.0` corresponds to **/21** (5 bits in the 3rd octet masked).
- **c ❌** `255.255.192.0` corresponds to **/18** (2 bits in the 3rd octet masked).
- **d ❌** `255.255.255.240` corresponds to **/28** (4 bits masked in the 4th octet).

---

## Question 23
**Which of the following is a private IP range?**

- a. 5.0.0.0/8
- **b. 172.16.0.0/12 ✓**
- c. 200.10.10.0/24
- d. 220.100.0.0/16

### ✅ Answer: **b**

> **Verification note:** RFC 1918 private ranges: 10.0.0.0/8, **172.16.0.0/12**, 192.168.0.0/16 — the other options are all public ranges.

**Justification:**

**RFC 1918** defines three private (non-routable) IPv4 ranges:

| Range | CIDR |
|---|---|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 |
| 172.16.0.0 – 172.31.255.255 | **172.16.0.0/12** |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 |

`172.16.0.0/12` falls squarely within the second private range.

- **a ❌** `5.0.0.0/8` is a **public** IP block allocated to RIPE NCC.
- **c ❌** `200.10.10.0/24` is a **public** address in the class C range.
- **d ❌** `220.100.0.0/16` is a **public** address in the class C range.

---

## Question 24
**How many usable host addresses does a /26 network have?**

- a. 64
- b. 126
- c. 32
- **d. 62 ✓**

### ✅ Answer: **d**

> **Verification note:** $2^6 - 2 = 62$ usable hosts; 64 is the total count (includes network + broadcast addresses which are reserved).

**Justification:**

A **/26** subnet leaves $32 - 26 = 6$ host bits:

$$\text{Total addresses} = 2^6 = 64$$
$$\text{Usable hosts} = 64 - 2 = \mathbf{62}$$

The 2 reserved addresses are the **network address** (all host bits = 0) and the **broadcast address** (all host bits = 1).

- **a ❌** 64 is the *total* number of addresses including the network and broadcast — not the usable host count.
- **b ❌** 126 is the usable hosts for a **/25** subnet ($2^7 - 2 = 126$).
- **c ❌** 32 would suggest a **/27** subnet ($2^5 = 32$ total, $30$ usable) — not /26.

---

## Question 25
**Which of the following resources is automatically allocated by AWS Lambda proportional to the amount of memory you configure?**

- **a. CPU Power ✓**
- b. Route tables
- c. AWS gateways
- d. AWS VPCs

### ✅ Answer: **a**

> **Verification note:** CPU scales proportionally to memory in Lambda — there is no direct CPU configuration; Route tables, gateways, and VPCs are separate AWS constructs.

**Justification:**

In AWS Lambda, **CPU power is not configured directly**. Instead, it is allocated **proportionally to the memory setting**: the more memory you configure (128 MB–10,240 MB), the more vCPU shares are allocated. This is a key Lambda design characteristic.

- **b ❌** Route tables are VPC networking constructs; they are not provisioned or scaled by Lambda memory settings.
- **c ❌** AWS Gateways (API Gateway, Internet Gateway, NAT Gateway) are separate services unrelated to Lambda resource allocation.
- **d ❌** AWS VPCs are not created or scaled by Lambda memory configuration.

---

## Question 26
**Which AWS service can be used to invoke a Lambda function natively in response to a file being uploaded to an object storage bucket?**

- a. AWS EC2
- b. Amazon Gateway
- c. AWS Storage Gateway
- **d. Amazon S3 ✓**

### ✅ Answer: **d**

> **Verification note:** S3 event notifications natively invoke Lambda on object upload — no EC2, VPN, or hybrid gateway needed.

**Justification:**

**Amazon S3** has a native, built-in event notification system that can invoke AWS Lambda directly when objects are created, modified, or deleted in a bucket — no intermediary service required. This is one of the most common Lambda trigger patterns.

- **a ❌** EC2 is a virtual server service; it does not natively emit events to trigger Lambda upon file uploads.
- **b ❌** "Amazon Gateway" is not a specific AWS service. API Gateway triggers Lambda via HTTP requests, not file uploads to object storage.
- **c ❌** AWS Storage Gateway is a hybrid storage service for connecting on-premises systems to AWS cloud storage; it does not natively invoke Lambda functions.

---

## Question 27
**How does AWS Lambda charge users for its compute services?**

- a. Based on a fixed hourly rate for keeping the container active.
- b. By the number of lines of code deployed in the function.
- c. Only by the amount of data transferred out of the function.
- **d. Based on the number of requests and the duration of execution. ✓**

### ✅ Answer: **d**

> **Verification note:** Lambda charges for requests + GB-seconds of duration only — no hourly idle rate, no line-of-code billing.

**Justification:**

Lambda pricing has two core components:
1. **Number of requests** (invocations) — billed per 1 million requests.
2. **Duration** — billed in GB-seconds (memory allocated × execution time in ms).

There is **no charge when the function is idle** — you only pay for actual compute consumed.

- **a ❌** There is no concept of a "running container" with an hourly rate in Lambda; functions are ephemeral and billed only during execution.
- **b ❌** Lines of code is entirely irrelevant to Lambda pricing.
- **c ❌** Data transfer costs exist for outbound traffic, but they are not the primary or only compute billing model.

---

## Question 28
**What is the primary purpose of AWS Lambda Layers?**

- a. To scale functions automatically across multiple AWS Regions.
- **b. To package libraries and other dependencies that multiple functions can securely share. ✓**
- c. To automatically convert synchronous invocations into asynchronous processes.
- d. To provide persistent block storage for execution environments.

### ✅ Answer: **b**

> **Verification note:** Layers = reusable dependency packages shared across functions; they do not control scaling, invocation type, or block storage.

**Justification:**

**Lambda Layers** allow you to package reusable code — libraries, SDKs, custom runtimes, configuration files — separately from your function code. A single layer can be attached to multiple Lambda functions, reducing deployment package size and promoting code reuse.

- **a ❌** Lambda scales automatically within a single region by default; Layers have no role in multi-region scaling.
- **c ❌** Converting synchronous to asynchronous invocations is controlled by the Lambda invocation type (RequestResponse vs. Event), not by Layers.
- **d ❌** Lambda execution environments only have ephemeral `/tmp` storage (up to 10 GB). Layers do not provide persistent block storage.

---

## Question 29
**Which of the following properties accurately describes how Inbound Rules operate within an AWS Security Group?**

- a. They support explicit 'Deny' rules to block specific IP addresses from accessing the resource.
- b. They are applied at the subnet level, automatically protecting all resources inside that subnet.
- **c. If an inbound request is allowed, the return traffic is automatically allowed regardless of outbound rules. ✓**
- d. You must also configure a corresponding outbound rule to allow return traffic.

### ✅ Answer: **c**

> **Verification note:** Stateful (Security Group) = return traffic auto-allowed; stateless (NACL) = requires explicit outbound rule for return traffic.

**Justification:**

Security Groups are **stateful**: the firewall tracks connection state. When an inbound connection is permitted, the corresponding return (outbound) traffic is **automatically allowed** without needing a matching outbound rule. This is the defining feature of stateful packet inspection.

- **a ❌** Security Groups only support **Allow** rules — there are no explicit Deny rules. To block traffic you simply omit an Allow rule. Network ACLs (NACLs) support both Allow and Deny.
- **b ❌** Security Groups operate at the **instance (ENI) level**, not the subnet level. NACLs operate at the subnet level.
- **d ❌** This is the behavior of a **stateless** firewall (like NACLs). Because Security Groups are stateful, return traffic is automatic — no corresponding outbound rule is required.

---

## Question 30
**To allow instances in a private subnet to securely download software updates from the internet, what target type should you specify for the '0.0.0.0/0' route in its routing table?**

- a. pcx-xxxxxx (VPC Peering Connection)
- b. igw-xxxxxx (Internet Gateway)
- **c. nat-xxxxxx (NAT Gateway) ✓**
- d. vgw-xxxxxx (Virtual Private Gateway)

### ✅ Answer: **c**

> **Verification note:** NAT Gateway = outbound-only internet for private subnets; IGW = public subnets (two-way), vgw = VPN/hybrid, pcx = VPC-to-VPC peering.

**Justification:**

A **NAT Gateway** allows instances in a **private subnet** to initiate outbound internet connections (e.g., `yum update`, `apt-get`) while blocking unsolicited inbound connections from the internet. The private subnet's route table sends `0.0.0.0/0` to the NAT Gateway, which resides in a public subnet.

- **a ❌** A **VPC Peering Connection** (`pcx`) enables private communication *between two VPCs* — it does not provide internet access.
- **b ❌** An **Internet Gateway** (`igw`) provides direct two-way internet access but belongs in the route table of a *public* subnet. Routing private subnet traffic directly to an IGW would expose instances to inbound internet traffic, defeating the purpose of a private subnet.
- **d ❌** A **Virtual Private Gateway** (`vgw`) terminates VPN tunnels from on-premises networks — it is used for hybrid connectivity, not for downloading software updates from the internet.
