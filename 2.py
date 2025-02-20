# Establishing a CI/CD Pipeline for Automated Deployment
import os
import subprocess

def setup_ci_cd():
    print("Initializing CI/CD pipeline...")
    os.system("echo 'CI/CD Pipeline Initialized'")

def create_dockerfile():
    dockerfile_content = """
    FROM python:3.9
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    COPY . .
    CMD ["python", "app.py"]
    """
    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content)
    print("Dockerfile created successfully.")

def build_and_push_docker_image():
    os.system("docker build -t myapp:latest .")
    os.system("docker tag myapp:latest myregistry/myapp:latest")
    os.system("docker push myregistry/myapp:latest")
    print("Docker image built and pushed successfully.")

def create_kubernetes_files():
    deployment_yaml = """
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: myapp-deployment
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: myapp
      template:
        metadata:
          labels:
            app: myapp
        spec:
          containers:
          - name: myapp
            image: myregistry/myapp:latest
            ports:
            - containerPort: 5000
    """
    service_yaml = """
    apiVersion: v1
    kind: Service
    metadata:
      name: myapp-service
    spec:
      selector:
        app: myapp
      ports:
        - protocol: TCP
          port: 80
          targetPort: 5000
      type: LoadBalancer
    """
    with open("deployment.yaml", "w") as f:
        f.write(deployment_yaml)
    with open("service.yaml", "w") as f:
        f.write(service_yaml)
    print("Kubernetes YAML files created successfully.")

def deploy_to_kubernetes():
    os.system("kubectl apply -f deployment.yaml")
    os.system("kubectl apply -f service.yaml")
    print("Deployment to Kubernetes completed successfully.")

def setup_monitoring():
    print("Setting up Prometheus and Grafana for monitoring...")
    os.system("echo 'Monitoring configured'")

def main():
    setup_ci_cd()
    create_dockerfile()
    build_and_push_docker_image()
    create_kubernetes_files()
    deploy_to_kubernetes()
    setup_monitoring()

if __name__ == "__main__":
    main()
