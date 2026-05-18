# High Performance & Distributed Computing — Session 23: Cloud Computing — Session 5 (Cell Counting with AWS Lambda)

**Date:** 2026-05-06 (Wed)
**Instructor:** Francesc Solsona Tehas (UAB)

---

## 1. Overview

This final cloud session demonstrates a **real-world healthcare application**: automated cell counting from medical images using **AWS Lambda** and **OpenCV**. The pipeline is fully serverless: images uploaded to S3 trigger Lambda functions that process them and store results.

---

## 2. Key Concepts

### 2.1 The Pipeline

1. **Input:** Medical images uploaded to an S3 bucket (`medical-images-input`)
2. **Trigger:** S3 upload event triggers a Lambda function
3. **Processing:** Lambda runs an OpenCV (CV2) script to count cells
4. **Output:** Processed results/images stored in another S3 bucket (`medical-images-output`)

### 2.2 AWS Lambda

- **Serverless compute** — no servers to manage
- Code runs in response to **triggers** (S3 events, API calls, etc.)
- Pay only for compute time used
- **Limitations:**
  - Execution timeout (max 15 minutes)
  - Limited libraries (no OpenCV by default)
  - Requires **Lambda Layers** for additional libraries

### 2.3 Lambda Layers

- **Problem:** OpenCV (CV2) is not available in the default Lambda runtime
- **Solution:** Create a **Lambda Layer** — a ZIP archive containing additional libraries
- **Steps:**
  1. Create a directory with Python 3.14
  2. Install OpenCV (`pip install opencv-python -t .`)
  3. Zip the entire directory → `opencv.zip`
  4. Upload to S3 (e.g., `layers-bucket/opencv.zip`)
  5. Attach the layer to the Lambda function

### 2.4 Complete Workflow

1. Create S3 buckets (input + output)
2. Create Lambda function with OpenCV layer
3. Upload images to input bucket → triggers Lambda
4. Lambda processes images (cell counting)
5. Results stored in output bucket

### 2.5 Commands Used

```bash
# Upload images to S3
aws s3 cp ./images/ s3://medical-images-input/ --recursive

# Copy Lambda layer to S3
aws s3 cp opencv.zip s3://layers-bucket/

# View processing results
aws s3 ls s3://medical-images-output/
```

---

## 3. Hands-on Completion

- Students are expected to **try the example** using their AWS credits (~€50)
- All steps are documented in the provided slides
- The demo shows the complete pipeline working end-to-end

---

## 4. Session Timeline

| Section | Time | Content |
|---------|------|---------|
| **I. Lambda Function Setup** | 0:14–49:00 | Creating Lambda, deploying code |
| **II. Lambda Layer for OpenCV** | 49:00–57:00 | Creating ZIP, uploading to S3, attaching |
| **III. Image Processing Demo** | 57:00–1:01 | Uploading images, triggering Lambda, results |
| **IV. Closing** | 1:01–1:02 | Course wrap-up |

---

## 5. Key Takeaways

- **AWS Lambda** enables serverless image processing pipelines
- **Lambda Layers** extend Lambda with custom libraries (e.g., OpenCV)
- The complete healthcare pipeline: **S3 → Lambda → S3**
- Serverless architectures are **scalable, cost-effective, and event-driven**
- Cloud computing enables **real-world medical image analysis** without managing infrastructure

---

*Sources: Transcript `2026_05_06_Cloud. Session 5_23.md`*
