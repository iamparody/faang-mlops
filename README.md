# FAANG Forecasting MLOps Project
<img width="600" height="306" alt="mlops-cycle" src="https://github.com/user-attachments/assets/a54a8e1f-98dc-4937-8071-ba95fb0b76aa" />


## Project Overview

A full-cycle MLOps project for FAANG stock price forecasting. Built to showcase core MLOps concepts like reproducibility, monitoring, CI/CD, and cloud readiness — all within a containerized setup. The project runs locally using Docker Compose and can be extended to cloud setups.

---
## 📌 Problem Statement
Stock prices for high-growth tech companies (FAANG) are volatile, influenced by global economic trends, sector-specific developments, and investor sentiment.
Accurately forecasting such prices is challenging but crucial for applications like:

### Algorithmic trading strategies
#### Portfolio risk management
#### Investment decision-making

This project tackles the challenge of building a fully reproducible, deployable, and monitored forecasting pipeline that predicts FAANG stock closing prices using Linear Regression.
Our goal was not just to build a model, but to design an MLOps-ready system that could be trained, deployed, and monitored in both local and cloud environments.

## 🎯 Project Goals
Develop a predictive model to forecast FAANG closing prices.
Implement MLOps best practices: reproducibility, CI/CD, monitoring, containerization.
Enable seamless deployment through Docker Compose with potential cloud migration.

## 🛠 Solution Approach
1. Data Exploration & Preparation
Collected historical FAANG stock price data.

Cleaned missing values, handled outliers, and engineered features (lag variables, rolling averages).

2. Model Selection & Training
Chose Linear Regression for its interpretability and quick iteration.

Used Scikit-Learn for training.

Logged experiments and metrics in MLflow.

3. Deployment
Built a FastAPI service for real-time predictions.

Containerized each service (model, monitoring, API) with Docker.

4. Monitoring
Used Evidently to detect data drift and monitor prediction quality.

Stored monitoring metrics in PostgreSQL and visualized them in Grafana.

5. CI/CD & Automation
Automated builds and tests with GitHub Actions.

Used Makefile for reproducible local workflows.

## 📁 Project Structure

```
faang-mlops/
├── orchestration/
│   ├── mlflow_pipeline/        # MLflow tracking & model training
│   ├── fastapi_app/            # FastAPI app for model serving
│   ├── monitoring/             # Evidently + Grafana setup
│   ├── data/                   # Reference and current CSV data for monitoring
│   ├── requirements.txt        # Python dependencies
│   └── Dockerfiles             # Each service has its own Dockerfile
├── docker-compose.yml         # Service orchestration
├── .env                       # Environment variables (not committed)
├── Makefile                   # Workflow automation
└── README.md
```

---

## ⚙️ Technologies Used

* **MLflow**: Model training, experiment tracking, and versioning
* **FastAPI**: REST API for model inference
* **Evidently**: Data and performance monitoring
* **Grafana + PostgreSQL**: Visualization of monitoring metrics
* **Docker + Docker Compose**: Container orchestration
* **Pandas & Scikit-Learn**: Data manipulation & ML modeling

---
## 📊 Results
Model: Linear Regression

Metrics: 6.7
Delivered an MLOps-ready stack that is fully containerized, version-controlled, and monitored.

## 🔬 1. Experimentation

**Objective:** Train a time-series regression model on FAANG stock data

### 🔧 Steps:

* Collected and preprocessed FAANG historical stock data
* Performed feature engineering (rolling averages, lags)
* Trained a linear regression model using Scikit-Learn
* Logged metrics and model to **MLflow**

### 🗂️ Key Files:

* `orchestration/mlflow_pipeline/train.py`
* `orchestration/mlflow_pipeline/config.yaml`
* `orchestration/mlflow_pipeline/utils.py`

### 🧠 Decisions:

* Chose linear regression for interpretability
* Used MLflow to version both metrics and artifacts

---

## 🚀 2. Deployment

**Objective:** Serve the trained model via REST API

### 🔧 Steps:

* Loaded the latest MLflow model from local `mlruns/`
* Created FastAPI endpoints for healthcheck and prediction
* Containerized with Docker

### 🗂️ Key Files:

* `orchestration/fastapi_app/main.py`
* `orchestration/fastapi_app/Dockerfile`

### 🔥 How to Run:

```bash
make build-fastapi
make run-fastapi
```

---

## 📊 3. Monitoring

**Objective:** Track data drift and prediction quality using **Evidently**

### 🔧 Steps:

* Compared `reference.csv` (baseline) vs `current.csv`
* Generated HTML and JSON monitoring reports
* Saved metrics to PostgreSQL
* Visualized in Grafana

### 🗂️ Key Files:

* `orchestration/monitoring/monitor.py`
* `orchestration/monitoring/grafana/` (dashboard config)
* `docker-compose.yml` (services)

### ⚠️ Known Issues:

* PostgreSQL SSL errors (solved by matching container names)
* Resource-intensive on low-spec machines

---

## 🧪 4. Testing

**Objective:** Ensure stability of the FastAPI prediction pipeline

### 🔧 Steps:

* Wrote unit test for `/predict` route using `pytest`
* Added pre-commit hooks for linting

### 🗂️ Key Files:

* `orchestration/fastapi_app/test_main.py`
* `.pre-commit-config.yaml`

---

## 🔁 5. Automation & CI/CD

**Objective:** Enable reproducible development and deployments

### 🔧 Steps:

* Added Makefile for repeatable workflows
* Defined GitHub Actions for lint, test, and build

### 🗂️ Key Files:

* `Makefile`
* `.github/workflows/ci.yml`

---

## 🧠 Key Lessons Learned

* Container isolation ensures reproducibility
* Evidently + Grafana provides powerful monitoring with minimal setup
* MLflow simplifies experiment tracking and version control
* Modular development aids debugging and future extensions

---

## 🧱 Future Improvements

* Use a lighter model (e.g., LightGBM or Ridge) for better performance
* Add support for cloud deployment (e.g., Render or LocalStack)
* Extend monitoring to support concept drift and multivariate alerts
* Improve model retraining pipeline with DAG (e.g., Mage or Airflow)

---

## 🌍 Author

**Kiriinya Antony**
MLOps | Data Engineering | Forecasting Systems

[LinkedIn](https://www.linkedin.com/in/antony-kiriinya-a45769211) | [GitHub](https://github.com/iamparody) | Nairobi, Kenya

---

## 📦 How to Run Entire Stack

```bash
# Build all services
make build-all OR docker compose up(from the root folder(faang-mlops))

# Start the stack (MLflow + FastAPI + Monitoring)
make up

# Open dashboards:
# MLflow:     http://localhost:5000
# FastAPI:    http://localhost:8000/docs
# Grafana:    http://localhost:3000 (admin/admin)
```
