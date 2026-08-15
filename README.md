# 🚀 Scalable Microservices with Docker & Kubernetes

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?logo=kubernetes)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)

---

## 📌 Project Overview

This project demonstrates a **scalable microservices application** built using **Python Flask, Docker, and Kubernetes**.

The application consists of three independent services:

- 🔹 **API Gateway**
- 👤 **User Service**
- 🛒 **Product Service**

The API Gateway acts as the main entry point and routes client requests to the appropriate backend microservice running inside the Kubernetes cluster.

---

## 🎯 Objectives

The main objectives of this project are:

- 🐳 Containerize applications using Docker
- 🔗 Build independent microservices
- 📦 Create and use a Docker Registry
- ☸️ Deploy services on Kubernetes
- 🌐 Configure Kubernetes networking
- 🔀 Implement API Gateway routing
- 📈 Run multiple replicas for scalability
- 🔍 Test communication between microservices

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Application Development |
| 🌶️ Flask | REST API |
| 🐳 Docker | Containerization |
| 📦 Docker Registry | Image Storage |
| ☸️ Kubernetes | Container Orchestration |
| 🖥️ Docker Desktop | Local Kubernetes Environment |
| 🌿 Git | Version Control |
| 🐙 GitHub | Source Code Management |

---

## 🏗️ Application Architecture

```text
                       👤 Client
                          |
                          ▼
                 ┌─────────────────┐
                 │   API Gateway   │
                 │     :5000       │
                 │   2 Replicas    │
                 └────────┬────────┘
                          |
                ┌─────────┴─────────┐
                ▼                   ▼
        ┌──────────────┐    ┌────────────────┐
        │ User Service │    │ Product Service│
        │    :5001     │    │      :5002     │
        │  2 Replicas  │    │   2 Replicas   │
        └──────────────┘    └────────────────┘
                          |
                          ▼
                 ☸️ Kubernetes Cluster
```

---

## 📂 Project Structure

```text
microservices-kubernetes/
│
├── 📁 api-gateway/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── 📁 user-service/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── 📁 product-service/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── 📁 k8s/
│   ├── api-gateway-deployment.yaml
│   ├── api-gateway-service.yaml
│   ├── user-deployment.yaml
│   ├── user-service.yaml
│   ├── product-deployment.yaml
│   └── product-service.yaml
│
├── .gitignore
└── README.md
```

---

# 🐳 Docker Setup

## Build Docker Images

### User Service

```bash
docker build -t user-service:latest ./user-service
```

### Product Service

```bash
docker build -t product-service:latest ./product-service
```

### API Gateway

```bash
docker build -t api-gateway:latest ./api-gateway
```

Check images:

```bash
docker images
```

---

## 📦 Local Docker Registry

A local Docker Registry was created to store the application images.

```bash
docker run -d --restart=always -p 5005:5000 --name registry registry:2
```

Verify:

```bash
docker ps --filter "name=registry"
```

### Tag Images

```bash
docker tag user-service:latest localhost:5005/user-service:latest

docker tag product-service:latest localhost:5005/product-service:latest

docker tag api-gateway:latest localhost:5005/api-gateway:latest
```

### Push Images

```bash
docker push localhost:5005/user-service:latest

docker push localhost:5005/product-service:latest

docker push localhost:5005/api-gateway:latest
```

---

# ☸️ Kubernetes Deployment

## Check Kubernetes Cluster

```bash
kubectl config current-context
```

```bash
kubectl get nodes
```

Expected:

```text
desktop-control-plane   Ready   control-plane
```

---

## 👤 Deploy User Service

```bash
kubectl apply -f k8s/user-deployment.yaml
kubectl apply -f k8s/user-service.yaml
```

---

## 🛒 Deploy Product Service

```bash
kubectl apply -f k8s/product-deployment.yaml
kubectl apply -f k8s/product-service.yaml
```

---

## 🚪 Deploy API Gateway

```bash
kubectl apply -f k8s/api-gateway-deployment.yaml
kubectl apply -f k8s/api-gateway-service.yaml
```

---

## 🔍 Verify Deployments

Check Deployments:

```bash
kubectl get deployments
```

Check Pods:

```bash
kubectl get pods
```

Check Services:

```bash
kubectl get services
```

### Expected Configuration

| Service | Type | Port | Replicas |
|---------|------|------|----------|
| 🚪 API Gateway | NodePort | 5000 → 30000 | 2 |
| 👤 User Service | ClusterIP | 5001 | 2 |
| 🛒 Product Service | ClusterIP | 5002 | 2 |

---

# 🧪 Testing

Port-forward the API Gateway:

```bash
kubectl port-forward service/api-gateway 8080:5000
```

---

## 🚪 API Gateway Test

```bash
curl.exe http://localhost:8080
```

### Response

```text
API Gateway is running!
```

---

## 👤 User Service Test

```bash
curl.exe http://localhost:8080/users
```

### Response

```json
{
  "service": "User Service",
  "users": [
    "Shivani",
    "Rahul",
    "Priya"
  ]
}
```

---

## 🛒 Product Service Test

```bash
curl.exe http://localhost:8080/products
```

### Response

```json
{
  "products": [
    {
      "id": 1,
      "name": "Laptop"
    },
    {
      "id": 2,
      "name": "Mobile"
    },
    {
      "id": 3,
      "name": "Keyboard"
    }
  ],
  "service": "Product Service"
}
```

---

# 📈 Scaling

Each service is configured with **2 replicas**.

```text
🚪 API Gateway       → 2 Replicas
👤 User Service      → 2 Replicas
🛒 Product Service   → 2 Replicas
```

To increase replicas:

```bash
kubectl scale deployment user-service --replicas=3
```

Verify:

```bash
kubectl get pods
```

Kubernetes automatically creates additional Pods according to the desired replica count.

---

# 🔗 Service Communication

The API Gateway communicates with the backend services using Kubernetes Service names.

```text
API Gateway
     |
     ├──► user-service:5001
     |
     └──► product-service:5002
```

This allows the API Gateway to communicate with the services without depending on individual Pod IP addresses.

---

# ✅ Final Result

The complete microservices application was successfully deployed and tested.

### ✔️ Completed

- 🐳 Dockerized all microservices
- 📦 Created local Docker Registry
- ☸️ Created Kubernetes cluster
- 🚀 Deployed User Service
- 🚀 Deployed Product Service
- 🚀 Deployed API Gateway
- 🔗 Configured Kubernetes Services
- 📈 Configured multiple replicas
- 🔀 Implemented API Gateway routing
- 🧪 Tested all API endpoints
- 🐙 Managed project using Git & GitHub

---

# 🎓 Key Learnings

Through this project, I gained practical experience with:

- Microservices Architecture
- Docker Containerization
- Docker Registry
- Kubernetes Deployments
- Kubernetes Services
- Kubernetes Networking
- Service Discovery
- API Gateway
- Application Scaling
- Git & GitHub

---

# 🏁 Conclusion

This project demonstrates how multiple independent services can be **containerized, deployed, connected, and scaled using Docker and Kubernetes**.

The successful end-to-end testing confirms that the API Gateway can communicate with both the User Service and Product Service through Kubernetes service discovery.

---

## 👩‍💻 Author

### **Shivani Bhosle**

**DevOps Project**

`Python` • `Flask` • `Docker` • `Kubernetes` • `Git` • `GitHub`

⭐ *Built as a hands-on DevOps project to practice container orchestration and scalable microservices deployment.*