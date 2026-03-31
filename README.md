# 🚀 Sentinel-Auth: Production-Ready 3-Tier Kubernetes Application with Observability

> **Sentinel-Auth is a fully containerized, secure authentication platform deployed on a local Minikube cluster. It integrates the "Golden Stack" (FastAPI, React, PostgreSQL) with a robust "Shift-Left" security pipeline and a unified observability layer, proving that enterprise-grade patterns can be validated locally for zero cost with real-time monitoring using Prometheus & Grafana.**

---
## 🏗️ Architecture Overview
<p align="center">
<img width="1408" height="768" alt="minikube arch" src="https://github.com/user-attachments/assets/3a483a19-09b3-47a8-8277-39197c41b4fb" />
</p>
```

---

## ⚙️ Tech Stack

| Layer         | Technology                   |
| ------------- | ---------------------------- |
| Frontend      | React + Axios                |
| Backend       | FastAPI (Python)             |
| Database      | PostgreSQL                   |
| Container     | Docker                       |
| Orchestration | Kubernetes (Minikube)        |
| Monitoring    | Prometheus + Grafana         |
| Deployment    | Helm (kube-prometheus-stack) |

---

## 🚀 Key Features

✅ User Registration System
✅ REST API with FastAPI
✅ Kubernetes Deployment (Pods, Services, PVC)
✅ Service Communication via Cluster DNS
✅ Prometheus Metrics (`/metrics` endpoint)
✅ Grafana Dashboard Visualization
✅ Real-time Request Monitoring
✅ Error Handling & Logging
✅ Debugged Real-World Issues (Networking, Routing, Metrics)

---

## 📊 Observability

* Integrated **Prometheus scraping** using ServiceMonitor
* Exposed application metrics via `/metrics`
* Built **Grafana dashboards** for:

  * Request rate
  * API usage
  * Latency insights
* Implemented **alert-ready monitoring setup**

---

## 🧠 Real-World Challenges Solved

| Problem                     | Solution                             |
| --------------------------- | ------------------------------------ |
| API 404 errors              | Fixed route prefix mismatch (`/api`) |
| Frontend runtime error      | Corrected request payload handling   |
| Kubernetes networking issue | Used Minikube service tunneling      |
| Metrics not visible         | Integrated Prometheus Instrumentator |
| Mixed pod versions          | Forced clean rebuild & rollout       |
| ServiceMonitor errors       | Installed kube-prometheus-stack      |

---

## 🛠️ Setup & Run Locally

### 1️⃣ Start Minikube

```bash
minikube start --driver=docker
```

### 2️⃣ Build Images

```bash
eval $(minikube docker-env)

docker build -t sentinel-backend ./app
docker build -t sentinel-frontend ./frontend
```

### 3️⃣ Deploy to Kubernetes

```bash
kubectl apply -f k3s/
```

### 4️⃣ Access Application

```bash
minikube service frontend-service
```

---

## 📊 Monitoring Setup

```bash
helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring --create-namespace

kubectl apply -f k3s/backend-monitor.yaml
```

### Access:

* Prometheus → `localhost:9090`
* Grafana → `localhost:3000`

---

## 📈 Example Prometheus Queries

```promql
rate(http_requests_total[1m])
```

```promql
http_requests_total
```

```promql
rate(http_request_duration_seconds_sum[1m]) 
/
rate(http_request_duration_seconds_count[1m])
```

---

## 💼 Skills Demonstrated

* Kubernetes (Deployments, Services, Networking)
* Docker & Containerization
* Microservices Architecture
* Monitoring & Observability
* Debugging Distributed Systems
* API Design & Integration
* DevOps Best Practices
---

## 🚀 Future Improvements

* 🔐 JWT Authentication (Login system)
* 🌐 Ingress Controller (Remove NodePort)
* 🔔 Alertmanager Integration (Email/Slack alerts)
* 📦 CI/CD Pipeline (GitHub Actions)
* 📜 Centralized Logging (Loki + Grafana)

---

## 👨‍💻 Author

**Akhil**
Aspiring Cloud & DevOps Engineer

---

## ⭐ If you found this useful

Give this repo a ⭐ and connect with me on LinkedIn!
