# HOL 02 — Deploying a Hybrid Infrastructure for Researchers in AWS

## All Commands Used (Step by Step)

---

## Pre-requisites

### A. AWS Academy Login

1. Go to [https://awsacademy.instructure.com/](https://awsacademy.instructure.com/) → **Student Login**
2. **Courses** → **AWS Academy Learner Lab** → **Modules** → **AWS Academy Learner Lab**
3. Click **Start Lab** → wait for green dot → click **AWS**

### B. Create SSH Key Pair (Local Machine)

```bash
mkdir -p ~/.ssh
ssh-keygen -t rsa -f ~/.ssh/aws-keypair
# Press Enter twice (no passphrase)
```

### C. Download Academy PEM Key (Alternative — Used in this lab)

From the Learner Lab page → **SSH key** → **Download PEM** → save it locally:

```bash
mv ~/Downloads/*.pem ~/.ssh/labsuser.pem
chmod 400 ~/.ssh/labsuser.pem
```

### D. Configure AWS CLI Credentials (Local Machine)

From the Learner Lab page → **AWS Details** → **Show** (next to AWS CLI) → copy the credentials block.

```bash
mkdir -p ~/.aws
nano ~/.aws/credentials
# Paste the credentials block:
# [default]
# aws_access_key_id=ASIA...
# aws_secret_access_key=...
# aws_session_token=...
# Save: Ctrl+X → Y → Enter
```

Verify credentials work:

```bash
aws sts get-caller-identity --region us-east-1
```

Disable AWS CLI pager (prevents output getting stuck):

```bash
export AWS_PAGER=""
```

---

## Step 1: Create VPC and Public Subnet

Create the Virtual Private Cloud with CIDR `10.0.0.0/16`:

```bash
aws ec2 create-vpc \
  --cidr-block 10.0.0.0/16 \
  --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=lab-vpc}]' \
  --region us-east-1
```

> **Output:** VPC ID = `vpc-054299b53c8363ddf`

Create the public subnet inside the VPC with CIDR `10.0.1.0/24`:

```bash
aws ec2 create-subnet \
  --vpc-id vpc-054299b53c8363ddf \
  --cidr-block 10.0.1.0/24 \
  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=lab-public-subnet}]' \
  --region us-east-1
```

> **Output:** Subnet ID = `subnet-02e67214ae0f03891`

Enable auto-assign public IP on the subnet (so EC2 instances get a public IP automatically):

```bash
aws ec2 modify-subnet-attribute \
  --subnet-id subnet-02e67214ae0f03891 \
  --map-public-ip-on-launch \
  --region us-east-1
```

---

## Step 2: Create and Attach Internet Gateway

Create the Internet Gateway (allows traffic between VPC and the internet):

```bash
aws ec2 create-internet-gateway \
  --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=lab-igw}]' \
  --region us-east-1
```

> **Output:** IGW ID = `igw-09e2b482861db90e9`

Attach the Internet Gateway to the VPC:

```bash
aws ec2 attach-internet-gateway \
  --internet-gateway-id igw-09e2b482861db90e9 \
  --vpc-id vpc-054299b53c8363ddf \
  --region us-east-1
```

---

## Step 3: Create Route Table

Create a route table for the public subnet:

```bash
aws ec2 create-route-table \
  --vpc-id vpc-054299b53c8363ddf \
  --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=lab-public-to-internet}]' \
  --region us-east-1
```

> **Output:** Route Table ID = `rtb-0862faf3b8ea8ca88`

Add a route to send all internet traffic (`0.0.0.0/0`) through the Internet Gateway:

```bash
aws ec2 create-route \
  --route-table-id rtb-0862faf3b8ea8ca88 \
  --destination-cidr-block 0.0.0.0/0 \
  --gateway-id igw-09e2b482861db90e9 \
  --region us-east-1
```

Associate the route table with the public subnet:

```bash
aws ec2 associate-route-table \
  --route-table-id rtb-0862faf3b8ea8ca88 \
  --subnet-id subnet-02e67214ae0f03891 \
  --region us-east-1
```

---

## Step 4: Launch EC2 Instance

Create a security group allowing SSH (port 22) and Jupyter (port 8888):

```bash
aws ec2 create-security-group \
  --group-name lab-sg \
  --description "HOL2 security group" \
  --vpc-id vpc-054299b53c8363ddf \
  --region us-east-1
```

> **Output:** Security Group ID = `sg-0cac6d1e0dddde0e0`

Open port 22 (SSH):

```bash
aws ec2 authorize-security-group-ingress \
  --group-id sg-0cac6d1e0dddde0e0 \
  --protocol tcp --port 22 \
  --cidr 0.0.0.0/0 \
  --region us-east-1
```

Open port 8888 (Jupyter Notebook):

```bash
aws ec2 authorize-security-group-ingress \
  --group-id sg-0cac6d1e0dddde0e0 \
  --protocol tcp --port 8888 \
  --cidr 0.0.0.0/0 \
  --region us-east-1
```

Find the latest Amazon Linux 2023 AMI:

```bash
aws ec2 describe-images \
  --owners amazon \
  --filters "Name=name,Values=al2023-ami-2023*-x86_64" "Name=state,Values=available" \
  --query 'Images | sort_by(@, &CreationDate) | [-1].ImageId' \
  --output text --region us-east-1
```

> **Output:** AMI ID = `ami-08e6829e013be2292`

Launch the EC2 instance using the Academy key pair (`vockey`):

```bash
aws ec2 run-instances \
  --image-id ami-08e6829e013be2292 \
  --instance-type t2.micro \
  --key-name vockey \
  --subnet-id subnet-02e67214ae0f03891 \
  --security-group-ids sg-0cac6d1e0dddde0e0 \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=lab-public-ec2}]' \
  --region us-east-1
```

> **Output:** Instance ID = `i-0ed6e53820503b73a`

Wait and get the public IP:

```bash
aws ec2 describe-instances \
  --instance-ids i-0ed6e53820503b73a \
  --query 'Reservations[0].Instances[0].PublicIpAddress' \
  --output text --region us-east-1
```

> **Output:** Public IP = `54.160.117.52`

---

## Step 5: SSH In and Install Software

Connect to the EC2 instance via SSH:

```bash
ssh -i ~/.ssh/labsuser.pem ec2-user@54.160.117.52
```

Update the system and install pip:

```bash
sudo yum update -y
sudo yum install python3-pip -y
```

Install required Python libraries (boto3, jupyter, pillow):

```bash
pip3 install boto3 jupyter pillow
```

---

## Step 6: Create S3 Buckets and Lambda Function

### 6a. Create S3 Buckets (from local terminal)

```bash
aws s3 mb s3://lab-input-bucket-arriazu --region us-east-1
aws s3 mb s3://lab-output-bucket-arriazu --region us-east-1
```

### 6b. Create Lambda Function Code

```bash
mkdir -p /tmp/lambda-hol2

cat > /tmp/lambda-hol2/lambda_function.py << 'EOF'
import boto3
import json
import os
import urllib.parse

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    original_name = os.path.splitext(os.path.basename(key))[0]
    download_path = f'/tmp/{os.path.basename(key)}'
    s3.download_file(bucket, key, download_path)

    result_image_name = f"{original_name}-processed.png"
    result_bucket = 'lab-output-bucket-arriazu'
    s3.upload_file(download_path, result_bucket, result_image_name)

    return {
        'statusCode': 200,
        'body': json.dumps(f"Processed {key}")
    }
EOF

cd /tmp/lambda-hol2 && zip lambda.zip lambda_function.py && cd -
```

### 6c. Get LabRole ARN and Create Lambda

```bash
aws iam get-role --role-name LabRole --query 'Role.Arn' --output text --region us-east-1
```

> **Output:** `arn:aws:iam::189775779298:role/LabRole`

```bash
aws lambda create-function \
  --function-name lab-lambda-function \
  --runtime python3.12 \
  --role arn:aws:iam::189775779298:role/LabRole \
  --handler lambda_function.lambda_handler \
  --zip-file fileb:///tmp/lambda-hol2/lambda.zip \
  --timeout 30 \
  --region us-east-1
```

### 6d. Add S3 Trigger to Lambda

Grant S3 permission to invoke the Lambda:

```bash
aws lambda add-permission \
  --function-name lab-lambda-function \
  --statement-id s3-trigger \
  --action lambda:InvokeFunction \
  --principal s3.amazonaws.com \
  --source-arn arn:aws:s3:::lab-input-bucket-arriazu \
  --region us-east-1
```

Configure S3 bucket to notify Lambda on new object creation:

```bash
aws s3api put-bucket-notification-configuration \
  --bucket lab-input-bucket-arriazu \
  --notification-configuration '{
    "LambdaFunctionConfigurations": [
      {
        "LambdaFunctionArn": "arn:aws:lambda:us-east-1:189775779298:function:lab-lambda-function",
        "Events": ["s3:ObjectCreated:*"]
      }
    ]
  }' \
  --region us-east-1
```

---

## Step 7: Configure AWS Credentials on EC2 and Launch Jupyter

### 7a. Configure AWS Credentials on EC2

On the EC2 instance (via SSH):

```bash
mkdir -p ~/.aws
nano ~/.aws/credentials
# Paste the same credentials block from AWS Details → Show
# Save: Ctrl+X → Y → Enter
```

### 7b. Launch Jupyter Notebook Server

```bash
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser
```

> **Output URL:** `http://54.160.117.52:8888/tree?token=d02478f86b786822670fa24ab1807fc08b455308784d386d`

### 7c. Run the Code in Jupyter

Open the URL in a browser → **New** → **Python 3** → paste and run:

```python
from PIL import Image, ImageDraw
import boto3
import io

image = Image.new('RGB', (200, 100), color='white')
draw = ImageDraw.Draw(image)
draw.text((50, 40), "Hello!", fill='black')
buffer = io.BytesIO()
image.save(buffer, format='PNG')
buffer.seek(0)

bucket_name = 'lab-input-bucket-arriazu'
s3 = boto3.client('s3')
object_key = 'lab-image.png'
s3.upload_fileobj(buffer, bucket_name, object_key)
print(f"Image uploaded to s3://{bucket_name}/{object_key}")
```

> **Output:** `Image uploaded to s3://lab-input-bucket-arriazu/lab-image.png`

---

## Step 8: Verify Lambda Processed the Image

Check the output bucket for the processed image:

```bash
aws s3 ls s3://lab-output-bucket-arriazu/ --region us-east-1
```

> **Output:** `2026-06-03 01:48:15  684 lab-image-processed.png` ✅

---

## Summary of Resources Created

| Resource | Name | ID |
|----------|------|----|
| VPC | `lab-vpc` | `vpc-054299b53c8363ddf` |
| Subnet | `lab-public-subnet` | `subnet-02e67214ae0f03891` |
| Internet Gateway | `lab-igw` | `igw-09e2b482861db90e9` |
| Route Table | `lab-public-to-internet` | `rtb-0862faf3b8ea8ca88` |
| Security Group | `lab-sg` | `sg-0cac6d1e0dddde0e0` |
| EC2 Instance | `lab-public-ec2` | `i-0ed6e53820503b73a` |
| S3 Input Bucket | `lab-input-bucket-arriazu` | — |
| S3 Output Bucket | `lab-output-bucket-arriazu` | — |
| Lambda Function | `lab-lambda-function` | — |

## Deliverable

- **PDF report** with screenshots of each step → send to `francesc.solsona@udl.cat`
