# 🏡 Predict My House Price API

A lightweight and explainable machine learning API that predicts California housing prices based on key demographic and geographic features. Powered by **Flask**, **scikit-learn**, and **Docker**, this project is designed to be modular, portable, and production-ready.

---

## 📈 Project Overview

This API is built to serve a trained regression model (e.g., `LinearRegression`) that predicts median house values using data from the California Housing Dataset. The project is structured for deployment via **Docker** and **Render**, and includes unit tests for API reliability.

---

## ⚙️ Features

- ✅ RESTful API built with Flask
- 🧠 ML model trained on California housing data
- 🐳 Dockerized for easy deployment
- 🧪 Unit tested with Pytest
- 🔍 Ready for explainability integration (e.g., SHAP, Lime)

---

## 🚀 Tech Stack

- Python 3.11  
- Flask  
- Scikit-learn  
- Pandas, NumPy  
- Docker  
- Pytest  

---

## 🧠 Input Features

| Feature      | Description                             |
|--------------|-----------------------------------------|
| `MedInc`     | Median income in the block              |
| `HouseAge`   | Median age of the house                 |
| `AveRooms`   | Average number of rooms per household   |
| `AveBedrms`  | Average number of bedrooms              |
| `Population` | Total population in the area            |
| `AveOccup`   | Average number of occupants per house   |
| `Latitude`   | Latitude of the area                    |
| `Longitude`  | Longitude of the area                   |

---

## 🛠 How to Run Locally

### 1. Clone the repository

git clone https://github.com/DanteTrb/predict-my-house-price.git
cd predict-my-house-price


### 🧱 2. Build Docker Image
bash
Copia
Modifica
docker build -t house-price-api .

## 🚀 3. Run the Docker Container
bash
Copia
Modifica
docker run -p 5050:5000 house-price-api
Your API will now be running locally at:
👉 http://localhost:5050

## 🧪 Run Unit Tests
Make sure you're in the project root and run:

bash
Copia
Modifica
PYTHONPATH=. pytest
📬 API Endpoint – /predict
Sends housing data and returns a price prediction.

## 🔹 Example POST Request
bash
Copia
Modifica
curl -X POST http://localhost:5050/predict \
  -H "Content-Type: application/json" \
  -d '{
        "MedInc": 8.3252,
        "HouseAge": 41.0,
        "AveRooms": 6.9841,
        "AveBedrms": 1.0238,
        "Population": 322.0,
        "AveOccup": 2.5556,
        "Latitude": 37.88,
        "Longitude": -122.23
      }'
🔸 Example Response
json
Copia
Modifica
{
  "prediction": 4.532
}
## 📦 Deployment Options
This app is ready to be deployed to:
🌐 [x] Render

📦 Deployment

This API is deployed and live at:

👉 [https://predict-my-house-price.onrender.com](https://predict-my-house-price.onrender.com)

You can test the `/predict` endpoint directly using:

bash
curl -X POST https://predict-my-house-price.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{ ... }'

---

## 🤝 Contributing
Contributions are welcome!
Feel free to fork the repo, submit issues or open PRs.

### 📫 Contact
Made with 💡 by Dante Trabassi
📧 Email: dantetrb@gmail.com
🔗 LinkedIn: linkedin.com/in/dantetrabassi