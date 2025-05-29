import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import os

def train_and_save_model():
    # 1. Carica il dataset
    df = pd.read_csv("data/housing.csv")

    # 2. Separazione input/output
    X = df.drop("MedHouseVal", axis=1)
    y = df["MedHouseVal"]

    # 3. Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Addestra il modello
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 5. Valutazione
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"✅ Modello addestrato. MSE: {mse:.4f}")

    # 6. Salva il modello
    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/house_price_model.pkl")
    print("📦 Modello salvato in model/house_price_model.pkl")

if __name__ == "__main__":
    train_and_save_model()