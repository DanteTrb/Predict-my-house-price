import joblib
import numpy as np

# Carica il modello salvato
model = joblib.load("model/house_price_model.pkl")

def predict_house_price(input_data: dict) -> float:
    features = [
        input_data["MedInc"],
        input_data["HouseAge"],
        input_data["AveRooms"],
        input_data["AveBedrms"],
        input_data["Population"],
        input_data["AveOccup"],
        input_data["Latitude"],
        input_data["Longitude"]
    ]

    input_array = np.array([features])
    prediction = model.predict(input_array)[0]  # warning ignorabile
    return prediction

# 🔍 Test locale
if __name__ == "__main__":
    sample_input = {
        "MedInc": 8.3252,
        "HouseAge": 41.0,
        "AveRooms": 6.9841,
        "AveBedrms": 1.0238,
        "Population": 322.0,
        "AveOccup": 2.5556,
        "Latitude": 37.88,
        "Longitude": -122.23
    }

    pred = predict_house_price(sample_input)
    print(f"🏠 Prezzo previsto: ${pred * 100000:.2f}")
