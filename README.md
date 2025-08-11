# FAANG Forecasting MLOps Project
<img width="600" height="306" alt="mlops-cycle" src="https://github.com/user-attachments/assets/a54a8e1f-98dc-4937-8071-ba95fb0b76aa" />


## Project Overview

A full-cycle MLOps project for FAANG stock price forecasting. Built to showcase core MLOps concepts like reproducibility, monitoring, CI/CD, and cloud readiness — all within a containerized setup. The project runs locally using Docker Compose and can be extended to cloud setups.

---
# Problem Statement
Financial market data, especially stock prices from high-growth tech companies (FAANG), is inherently noisy, non-stationary, and influenced by a variety of economic, technological, and social factors.
Accurately forecasting such time series data is a challenging task, yet it is critical for informed decision-making in areas such as algorithmic trading, risk management, and portfolio optimization.

In this project, I aimed to build an end-to-end ARIMA/SARIMA forecasting pipeline for the FAANG dataset, focusing on:

Understanding the underlying time series behavior (stationarity, seasonality, autocorrelation patterns).

Selecting optimal model parameters through statistical tests (ADF, ACF, PACF) and iterative experimentation.

Evaluating forecast performance with metrics such as MSE, RMSE, and Ljung–Box test for residual autocorrelation.

Reproducibility and deployment readiness, so that the model can be integrated into larger MLOps workflows.

I approached the problem by systematically moving through:

Data Exploration & Cleaning – Understanding missing values, trends, and outliers in FAANG closing price data.

Stationarity Checks & Transformation – Applying differencing and log transformations to stabilize variance and mean.

Parameter Selection – Using ACF/PACF plots to inform (p, d, q) choices.

Model Training & Residual Diagnostics – Ensuring the model assumptions were met and refining parameters when residual patterns were detected.

Evaluation & Interpretation – Comparing model predictions against actual values and assessing statistical robustness.

Future Work – Scaling the pipeline, integrating with MLflow for tracking, and containerizing for deployment.

Through this structured approach, I addressed the problem of building a reliable, statistically sound forecasting pipeline that balances predictive accuracy with interpretability — a key requirement for practical financial forecasting systems.

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
