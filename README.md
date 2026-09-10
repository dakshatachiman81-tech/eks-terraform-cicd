# EKS Terraform CI/CD Platform

> **End-to-End AWS DevOps Deployment using Terraform, Amazon EKS, Docker, Amazon ECR, GitHub Actions, and GitHub OIDC**

An end-to-end DevOps implementation that provisions AWS infrastructure using **Terraform** and automates containerized application deployment to **Amazon EKS** through a secure **GitHub Actions CI/CD pipeline**.

The project demonstrates Infrastructure as Code, container orchestration, cloud-native deployment, AWS IAM/OIDC authentication, Kubernetes Ingress, and automated application delivery.

---

## 📌 Overview

This project implements a production-oriented deployment workflow for a Flask web application running on Amazon EKS.

Infrastructure is provisioned using Terraform, application images are stored in Amazon ECR, and GitHub Actions automatically builds, publishes, and deploys new application versions to the EKS cluster.

### Deployment Flow

```text
Developer
    │
    │ Git Push
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    │ GitHub OIDC
    ▼
AWS IAM Role
    │
    ├──────────────► Amazon ECR
    │                   │
    │                   │ Docker Image
    │                   ▼
    └──────────────► Amazon EKS
                        │
                        ▼
                  Kubernetes Deployment
                        │
                        ▼
                  Kubernetes Service
                        │
                        ▼
                   ALB Ingress
                        │
                        ▼
                 AWS Application
                  Load Balancer
                        │
                        ▼
                    End User
```

---

## 🏗️ Architecture

The solution consists of the following major components:

| Layer              | Technology                   | Purpose                              |
| ------------------ | ---------------------------- | ------------------------------------ |
| Application        | Python / Flask               | Web application                      |
| Containerization   | Docker                       | Package application and dependencies |
| IaC                | Terraform                    | Provision AWS infrastructure         |
| Container Registry | Amazon ECR                   | Store Docker images                  |
| Orchestration      | Amazon EKS                   | Run and manage containers            |
| Networking         | Amazon VPC                   | Provide isolated AWS networking      |
| Ingress            | AWS Load Balancer Controller | Provision and manage ALB             |
| Load Balancing     | Application Load Balancer    | Expose application externally        |
| CI/CD              | GitHub Actions               | Automate build and deployment        |
| Authentication     | GitHub OIDC + AWS IAM        | Secure AWS authentication            |
| Configuration      | Kubernetes manifests         | Define application resources         |

---

## ☁️ AWS Infrastructure

The infrastructure is provisioned using Terraform.

### AWS Region

```text
ap-south-1
```

### EKS Cluster

```text
devops-eks-cluster
```

### ECR Repository

```text
devops-eks-app
```

### Infrastructure Components

* Amazon VPC
* Public and private subnets
* Internet Gateway
* NAT Gateway
* Security Groups
* Amazon EKS Cluster
* EKS Worker Nodes
* AWS IAM configuration
* Amazon ECR
* AWS Load Balancer Controller
* Application Load Balancer

---

## 📁 Repository Structure

```text
eks-terraform-cicd/
│
├── Application/
│   ├── app.py
│   └── Dockerfile
│
├── Kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
│
├── Terraform/
│   ├── provider.tf
│   ├── terraform.tf
│   ├── variable.tf
│   ├── vpc.tf
│   └── eks.tf
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
└── README.md
```

---

# 🏗️ Infrastructure as Code

Terraform is used to provision and manage the AWS infrastructure.

The Terraform configuration manages the core infrastructure required for the EKS environment, including:

* VPC networking
* Subnets
* Internet Gateway
* NAT Gateway
* Security Groups
* EKS cluster
* Worker nodes
* IAM-related configuration

### Terraform Workflow

```bash
terraform init
terraform validate
terraform plan
terraform apply
```

Terraform provides a repeatable and version-controlled approach to infrastructure provisioning.

---

# 🐳 Containerization

The Flask application is packaged into a Docker container.

Application directory:

```text
Application/
```

The Docker image is built from the project's Dockerfile.

Example:

```bash
docker build -t devops-eks-app ./Application
```

The image is then tagged and pushed to Amazon ECR.

---

# 📦 Amazon ECR

Amazon Elastic Container Registry is used as the private container registry.

Repository:

```text
devops-eks-app
```

Each CI/CD execution creates image versions using:

```text
<GitHub Commit SHA>
latest
```

Using the Git commit SHA provides traceability between:

```text
Git Commit
     ↓
Docker Image
     ↓
ECR
     ↓
Kubernetes Deployment
```

This makes it possible to identify exactly which source-code version is running in the cluster.

---

# ☸️ Amazon EKS

The application is deployed to an Amazon EKS cluster using Kubernetes.

### Deployment

```text
Name: devops-eks-app
Replicas: 2
```

Two replicas provide basic application redundancy and allow Kubernetes to maintain the desired number of running pods.

### Service

```text
Name: devops-eks-service
Type: ClusterIP
Port: 80
```

The Kubernetes Service provides internal connectivity between the Ingress layer and application pods.

---

# 🌐 Kubernetes Ingress & AWS ALB

External application access is implemented using the **AWS Load Balancer Controller** and Kubernetes Ingress.

### Ingress

```text
Name: devops-eks-ingress
Class: alb
```

Traffic flow:

```text
Internet
   │
   ▼
Application Load Balancer
   │
   ▼
Kubernetes Ingress
   │
   ▼
Kubernetes Service
   │
   ▼
Flask Pods
```

The AWS Load Balancer Controller automatically provisions and configures the Application Load Balancer based on the Kubernetes Ingress resource.

---

# 🔐 GitHub OIDC & AWS IAM

The CI/CD pipeline uses **GitHub OIDC federation** to authenticate with AWS.

No long-lived AWS access keys are required in GitHub Actions.

### Authentication Flow

```text
GitHub Actions
      │
      ▼
GitHub OIDC Token
      │
      ▼
AWS IAM OIDC Provider
      │
      ▼
IAM Role
      │
      ▼
Temporary AWS Credentials
      │
      ▼
AWS Services
```

IAM role:

```text
GitHubActions-EKS-CICD
```

The IAM trust relationship restricts the role to the intended GitHub repository and branch.

This improves security by avoiding the storage of permanent AWS credentials in GitHub.

---

# 🔄 CI/CD Pipeline

The complete application deployment is automated through GitHub Actions.

Workflow:

```text
.github/workflows/deploy.yml
```

### Pipeline Stages

```text
1. Checkout Source Code
          ↓
2. Authenticate with AWS using OIDC
          ↓
3. Verify AWS Identity
          ↓
4. Authenticate with Amazon ECR
          ↓
5. Build Docker Image
          ↓
6. Tag Image
          ↓
7. Push Image to ECR
          ↓
8. Configure kubectl for EKS
          ↓
9. Verify EKS Connectivity
          ↓
10. Update Kubernetes Deployment
          ↓
11. Monitor Rollout
          ↓
12. Verify Running Pods
```

---

# 🚀 Automated Deployment

Whenever code is pushed to the `main` branch, GitHub Actions automatically starts the deployment pipeline.

The Kubernetes deployment is updated with the newly created ECR image:

```bash
kubectl set image deployment/devops-eks-app \
  devops-eks-app=<ECR_IMAGE>:<GITHUB_SHA>
```

The pipeline then validates the rollout:

```bash
kubectl rollout status deployment/devops-eks-app
```

This ensures that the workflow does not finish successfully until the new application version has been successfully rolled out.

---

# 🔎 Deployment Verification

### Check EKS nodes

```bash
kubectl get nodes
```

### Check deployment

```bash
kubectl get deployment devops-eks-app
```

Expected:

```text
READY   2/2
```

### Check pods

```bash
kubectl get pods
```

Expected:

```text
devops-eks-app-xxxxx   1/1   Running
devops-eks-app-xxxxx   1/1   Running
```

### Check service

```bash
kubectl get svc
```

### Check ingress

```bash
kubectl get ingress
```

### Verify the deployed image

```bash
kubectl get deployment devops-eks-app \
  -o jsonpath="{.spec.template.spec.containers[0].image}"
```

---

# 🧪 CI/CD Validation

The CI/CD pipeline was validated by modifying the application version and pushing the change to the `main` branch.

Example application version:

```html
<title>DevOps Cloud Platform - v3</title>
```

After the Git push:

```text
Git Push
   ↓
GitHub Actions
   ↓
Docker Build
   ↓
ECR Push
   ↓
EKS Authentication
   ↓
Kubernetes Deployment Update
   ↓
Rollout Verification
   ↓
Updated Application
```

The updated application was successfully served through the AWS Application Load Balancer.

---

# 🛡️ Security Considerations

The project incorporates the following security practices:

* GitHub OIDC authentication
* AWS IAM role-based access
* Temporary AWS credentials
* Repository-specific IAM trust policy
* ECR private image registry
* EKS Access Entry for CI/CD authorization
* No permanent AWS access keys stored in GitHub
* Kubernetes-based application isolation
* IAM permissions scoped to required AWS resources

---

# 📊 Key DevOps Concepts Demonstrated

This project demonstrates practical implementation of:

### AWS

* Amazon VPC
* Amazon EKS
* Amazon ECR
* AWS IAM
* AWS Load Balancer Controller
* Application Load Balancer

### Infrastructure as Code

* Terraform
* Infrastructure provisioning
* Infrastructure version control
* Repeatable deployments

### Containers

* Docker
* Container image management
* Amazon ECR

### Kubernetes

* Deployments
* Pods
* Services
* Ingress
* Replica management
* Rollout verification

### CI/CD

* GitHub Actions
* Automated Docker builds
* Automated ECR publishing
* Automated EKS deployment
* Deployment verification

### Cloud Security

* GitHub OIDC
* AWS IAM
* Temporary credentials
* EKS Access Entry

---

# 🎯 Project Outcome

The final implementation provides a complete automated delivery pipeline where a code change pushed to GitHub can be automatically:

```text
Built
  ↓
Containerized
  ↓
Published to ECR
  ↓
Deployed to EKS
  ↓
Validated
  ↓
Exposed through AWS ALB
```

This eliminates the need for manual Docker image publishing and manual Kubernetes deployment for every application change.

---

# 💡 Skills Demonstrated

**AWS | Amazon EKS | Amazon ECR | Terraform | Kubernetes | Docker | GitHub Actions | GitHub OIDC | AWS IAM | VPC | ALB | Linux | CI/CD | Infrastructure as Code**

---

## 👩‍💻 Author

**Dakshata Chiman**

Cloud & DevOps Engineer

Focused on **AWS Cloud, DevOps, Kubernetes, Terraform, CI/CD, and Cloud Infrastructure**.
