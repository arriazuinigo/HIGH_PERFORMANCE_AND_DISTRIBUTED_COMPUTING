# High Performance & Distributed Computing — Session 22: Cloud Computing — Session 4

**Date:** 2026-04-29 (Wed)
**Instructor:** Francesc Solsona Tehas (UAB)

---

## 1. Overview

This hands-on session focuses on **AWS S3 (Simple Storage Service)** and how to read/write files to S3 buckets using **Boto3** (the AWS SDK for Python). The session also covers **AWS Lambda** concepts.

---

## 2. Key Concepts

### 2.1 AWS S3 (Simple Storage Service)

- **Object storage** service for storing and retrieving any amount of data
- Data is stored in **buckets** (containers)
- Files are accessed via **keys** (paths)
- Common for: data lakes, backups, static website hosting, big data analytics

### 2.2 Reading Files from S3 with Python (Boto3)

```python
import boto3

s3 = boto3.client('s3')
response = s3.get_object(Bucket='my-bucket', Key='path/to/file.txt')
content = response['Body'].read().decode('utf-8')
print(content)
```

### 2.3 Writing Files to S3 with Python (Boto3)

```python
import boto3

s3 = boto3.client('s3')
s3.put_object(
    Bucket='my-bucket',
    Key='path/to/output.txt',
    Body='Hello, S3!'
)
```

### 2.4 Key S3 Operations

| Operation | Description |
|-----------|-------------|
| `s3.list_buckets()` | List all buckets |
| `s3.list_objects(Bucket='name')` | List objects in a bucket |
| `s3.get_object(Bucket, Key)` | Read a file |
| `s3.put_object(Bucket, Key, Body)` | Write a file |
| `s3.upload_file(local_path, Bucket, Key)` | Upload a local file |

### 2.5 AWS Lambda (Preview)

- **Serverless compute** service
- Run code without provisioning servers
- Triggered by events (e.g., file upload to S3)
- Will be covered in the next session with image processing

---

## 3. Lab 1 Reminder

- **Deadline:** May 6th
- Students must submit their personal website link on the course main page

---

## 4. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. S3 Reading Demo** | 1:17–1:20 | Reading files from S3 with Boto3 |
| **II. S3 Writing Demo** | 1:20–1:26 | Writing files to S3 with Boto3 |
| **III. Lambda Preview** | 1:26–1:27 | Introduction to serverless computing |

---

## 5. Key Takeaways

- **S3** is AWS's object storage service (buckets + keys)
- **Boto3** is the Python SDK for AWS
- S3 is commonly used for **data lakes** and **cloud-native storage**
- **Lambda** enables serverless event-driven computing
- Lab 1 deadline: **May 6th**

---

*Sources: Transcript `2026_04_29_Cloud. Session 4_22.md`*
