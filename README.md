# AWS Cloud Resume Challenge

## Overview

The **AWS Cloud Resume Challenge** is a hands-on project designed to demonstrate my expertise in cloud technologies, infrastructure-as-code, and full-stack development. This project aligns with my goal of building scalable, secure, and performant solutions in the cloud while applying DevOps best practices.

---

## Features

- **Responsive Front-End**: A personal resume website built with HTML and CSS, hosted on **AWS S3** with static website hosting.
- **Global Content Delivery**: Accelerated using **Amazon CloudFront**, ensuring fast load times worldwide.
- **Custom Domain**: Configured with **Amazon Route 53** for DNS management and a professional, custom URL.
- **Back-End Integration**: Built an API using **AWS Lambda** and **API Gateway** to track visitor counts dynamically.
- **Infrastructure as Code**: Deployed infrastructure using **Terraform** to manage resources as code for repeatability and version control.
- **CI/CD Pipeline**: Streamlined deployment using GitHub Actions for automated updates to both the front-end and back-end components.
- **Serverless Architecture**: Leveraged serverless computing for scalability and cost-efficiency.

---

## Technologies Used

- **Cloud Providers**: AWS (S3, Lambda, API Gateway, CloudFront, Route 53, IAM)
- **Infrastructure as Code (IaC)**: Terraform
- **Programming Languages**: Python (for Lambda), HTML, CSS
- **DevOps Tools**: GitHub Actions
- **Version Control**: Git, GitHub

---

## Architecture Diagram

_[in progress...]_

---

## Project Breakdown

1. **Static Website Setup**:
   - Developed the front-end in HTML and CSS.
   - Deployed to AWS S3 with public access blocked, serving content via CloudFront.
   - Configured a custom domain using Route 53.

2. **Back-End API**:
   - Created a serverless API using AWS Lambda and API Gateway.
   - Wrote Python code to connect the API to a DynamoDB table, recording visitor counts.
   - Secured API endpoints with appropriate IAM roles.

3. **Infrastructure as Code**:
   - Used Terraform to define and deploy all AWS resources.
   - Applied best practices in resource organization and modularity.

4. **CI/CD Pipeline**:
   - Configured GitHub Actions workflows for automated testing and deployment.
   - Enabled seamless updates to both the front-end and back-end.

---

## Challenges and Learnings

- Migrating from AWS SAM to **Terraform** for better flexibility in infrastructure management.
- Debugging and resolving IAM policy issues to ensure secure resource access.
- Addressing GitHub's file size restrictions and learning advanced Git techniques like BFG for repository cleanup.

---

## How to Use

1. Clone the repository:
```
git clone https://github.com/swejoycechoi/aws_cloud_resume_challenge.git
```

2. Navigate to the project directory:
```
cd aws_cloud_resume_challenge
```

3. Deploy the infrastructure:
```
terraform init
terraform plan
terraform apply
```

4. Visit the deployed website to see the project live
```
https://www.swejoyce.com
```