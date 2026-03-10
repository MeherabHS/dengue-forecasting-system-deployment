#  Dengue Case Forecasting System

A deployed statistical forecasting system designed to estimate **next-month dengue incidence** using historical epidemiological data and seasonal time-series modeling.

The system integrates a **Seasonal ARIMA (SARIMA) forecasting model**, a **FastAPI inference service**, and a **Streamlit visualization dashboard** to deliver an end-to-end predictive analytics pipeline for dengue surveillance.

This project demonstrates a **complete machine learning deployment workflow**, including:

- Time-series model training and validation
- Model inference service through a REST API
- Cloud-deployed backend architecture
- Interactive dashboard visualization
- Automated forecast generation and logging

The goal of this system is to illustrate how statistical forecasting models can be operationalized into **real-world analytical tools for epidemiological monitoring and decision support**.

---

#  Live Deployment

### Interactive Dashboard
https://dengue-7zv7elbpptgrqmzrpmhlou.streamlit.app

### Forecast API Endpoint
https://dengue-yecr.onrender.com/forecast

### API Health Check
https://dengue-yecr.onrender.com/health

---

#  Key Features

-  Automated **next-month dengue incidence prediction**
-  Forecast **95% confidence intervals**
-  RESTful **model inference API**
-  Interactive **Streamlit visualization dashboard**
-  Automated **forecast generation and logging pipeline**
-  Modular **ML system architecture**

---

#  Model Overview

The forecasting model is based on a **Seasonal ARIMA (SARIMA)** time-series specification trained on historical dengue incidence data.

### Model Specification

```
SARIMA(1,1,1)(1,1,1,12)
```

### Target Variable

```
log(1 + dengue_total_cases)
```

A logarithmic transformation is applied to stabilize variance and improve model stability.

Predictions are converted back to case counts using:

```
cases = exp(prediction) - 1
```

---

#  System Architecture

```
Historical Dengue Dataset
        │
        ▼
 model_training.py
        │
        ▼
 Trained Model Artifact
 artifacts/sarima_model.pkl
        │
        ▼
 model_forecast.py
        │
        ▼
 FastAPI Backend Service
 api_server.py
        │
        ▼
 REST API Endpoints
 /forecast   /health
        │
        ▼
 Streamlit Dashboard
 dashboard.py
        │
        ▼
 User Interface
```

---

#  Project Structure

```
dengue-forecast/
│
├── api_server.py
├── dashboard.py
├── model_forecast.py
├── model_training.py
├── update_pipeline.py
│
├── artifacts/
│   ├── sarima_model.pkl
│   └── model_metadata.json
│
├── dengue dataset.csv
├── requirements.txt
└── README.md
```

---

#  Installation (Local Setup)

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/dengue-forecast.git
cd dengue-forecast
```

Install dependencies:

```
pip install -r requirements.txt
```

---

#  Running the System Locally

## Start the API Server

```
python -m uvicorn api_server:app --host 0.0.0.0 --port 8000 --reload
```

Test the API:

```
http://127.0.0.1:8000/forecast
```

---

## Launch the Dashboard

```
python -m streamlit run dashboard.py
```

Open in browser:

```
http://localhost:8501
```

---

#  Automated Forecast Pipeline

The project includes an automated script that generates and logs updated forecasts.

Run:

```
python update_pipeline.py
```

This process will:

1. Generate a new dengue forecast
2. Append results to the forecast log file:

```
forecast_log.csv
```

Example output:

```
timestamp,predicted_cases,lower_bound,upper_bound
2026-03-10T17:21:15Z,359.6,79.4,1617.2
```

---

#  Example Forecast Output

| Metric | Value |
|------|------|
| Predicted Cases | **359.6** |
| Lower Bound | **79.4** |
| Upper Bound | **1617.2** |

The wide confidence interval reflects **uncertainty in dengue transmission dynamics and seasonal variability**.

---

#  Deployment

The system follows a **two-tier cloud deployment architecture**.

### Backend Service

FastAPI application deployed on **Render**

Start command:

```
uvicorn api_server:app --host 0.0.0.0 --port $PORT
```

### Frontend Dashboard

Streamlit application deployed on **Streamlit Community Cloud**

Environment variable configuration:

```
API_BASE_URL = "https://dengue-yecr.onrender.com"
```

---

#  Technologies Used

- Python
- FastAPI
- Streamlit
- Statsmodels
- Pandas
- NumPy
- Scikit-learn
- Uvicorn

---

#  Future Improvements

- Integration of climate covariates (rainfall, temperature, humidity)
- Multi-city dengue forecasting framework
- Weekly resolution forecasts
- Deep learning model comparison (LSTM / Transformer)
- Real-time epidemiological data ingestion

---

# 📄 License

MIT License

---

#  Author

**Meherab Hossain Shafin**  


Daffodil International University 
Bangladesh
