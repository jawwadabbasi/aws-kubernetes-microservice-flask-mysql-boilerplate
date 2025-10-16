# aws-kubernetes-microservice-flask-mysql-boilerplate

A production-ready Flask microservice boilerplate designed for scalable deployments on AWS EKS (Kubernetes) with MySQL and CI/CD via GitHub Actions. 
This boilerplate follows a clean, modular structure that separates development and production environments, ensuring seamless builds and deployments across stages.

---

## Key Features

- Flask-based Microservice Architecture
  - Organized into API versions (v1, v2) with controllers and wrappers.
  - Supports modular endpoint structure for future scalability.

- MySQL Database Integration
  - Uses a lightweight includes/db.py connector.
  - Schema management via includes/schema.py.

- Environment-specific Configurations
  - dev/settings.py and prod/settings.py are copied automatically during build.
  - The correct configuration is selected based on the Git branch (dev or main).

- Containerization
  - Each environment (dev and prod) contains its own Dockerfile and Kubernetes manifest (kubeconfig.yaml).
  - Built with clean layering and environment variables baked into settings.

- CI/CD with GitHub Actions
  - Automated build, test, and deploy pipeline.
  - Validates Python code syntax.
  - Builds Docker image and pushes to AWS ECR.
  - Deploys to AWS EKS via kubectl.

- AWS Integration
  - Fully automated EKS deployment with namespace and image placeholders.
  - Uses AWS Secrets Manager for credentials and AWS ECR for Docker image storage.

---

## Folder Structure

```
├── .github
│   └── workflows
│       ├── dev.yaml
│       └── prod.yaml
├── dev
│   ├── Dockerfile
│   ├── kubeconfig.yaml
│   └── settings.py
├── prod
│   ├── Dockerfile
│   ├── kubeconfig.yaml
│   └── settings.py
└── src
    ├── configure.py
    ├── cron.py
    ├── includes
    │   ├── common.py
    │   ├── db.py
    │   └── schema.py
    ├── main.py
    ├── requirements.txt
    ├── services
    │   ├── crons.py
    │   └── logger.py
    ├── v1
    │   ├── api.py
    │   ├── controller.py
    │   └── wrapper.py
    └── v2
        └── controller.py
```
---

## Setting Up AWS & GitHub Secrets

Before your first deployment, configure the following GitHub Actions Secrets:

| Secret Name | Description |
|--------------|-------------|
| AWS_ACCESS_KEY_ID | AWS IAM access key |
| AWS_SECRET_ACCESS_KEY | AWS IAM secret key |
| AWS_REGION | AWS region where your EKS cluster resides |
| AWS_DOCKER_REGISTRY | AWS ECR repository URI |
| AWS_PROD_CLUSTER_01 | Base64-encoded kubeconfig for your EKS cluster |
| KUBE_NAMESPACE | Kubernetes namespace (e.g., prod-namespace) |

Ensure your AWS IAM user has ECR and EKS permissions.

---

## Local Development

cd src
pip install -r requirements.txt
python main.py

Then open: http://localhost:8000/api/v1/your-endpoint

---

## License

This project is licensed under the MIT License — free for personal and commercial use.