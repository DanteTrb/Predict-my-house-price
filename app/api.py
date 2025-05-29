from flask import Flask, request, jsonify
from app.predict import predict_house_price

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "🏠 Benvenuto nell'API di House Price Predictor!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.get_json()

        # Validazione input
        expected_keys = [
            "MedInc", "HouseAge", "AveRooms", "AveBedrms",
            "Population", "AveOccup", "Latitude", "Longitude"
        ]
        if not all(k in input_data for k in expected_keys):
            return jsonify({"error": "Input incompleto o scorretto"}), 400

        prediction = predict_house_price(input_data)
        return jsonify({"predicted_price": round(prediction * 100000, 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)