# Student Task Manager

## Project Overview
Student Task Manager is a web application that helps students manage
academic tasks. Users can add tasks and mark tasks as completed.

## Technologies Used
- Python
- Flask
- Pytest
- Docker
- Jenkins
- Kubernetes
- Minikube
- GitHub
- Docker Hub

## Application Features
- Display academic tasks
- Add new tasks
- Mark tasks as completed
- Health-check endpoint

## CI/CD Pipeline
1. Checkout source code from GitHub.
2. Install dependencies and run tests.
3. Build a Docker image.
4. Push the image to Docker Hub.
5. Deploy the application to Minikube.
6. Verify the Kubernetes deployment and application.

## Kubernetes Files
- k8s/deployment.yaml
- k8s/service.yaml

## Health Check
The application health endpoint is /health.
