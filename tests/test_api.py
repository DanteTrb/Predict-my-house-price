import pytest
from app.api import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"House Price Predictor" in response.data

def test_predict_route(client):
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
    response = client.post("/predict", json=sample_input)
    assert response.status_code == 200
    data = response.get_json()
    assert "predicted_price" in data
    assert isinstance(data["predicted_price"], float)