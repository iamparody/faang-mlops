import pandas as pd
import numpy as np
import mlflow
import yaml
import sys
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from mlflow.models import infer_signature

def load_config(config_path):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def train_model(config_path):
    config = load_config(config_path)

    mlflow.set_tracking_uri(config["tracking_uri"])  # http://mlflow-tracking:5000
    try:
        mlflow.set_experiment(config["experiment_name"])
    except Exception as e:
        print(f"Error setting experiment: {e}")
        sys.exit(1)

    df = pd.read_csv(config["data_path"])

    if 'Prev_Close' in config['features']:
        df['Prev_Close'] = df.groupby('Ticker')['Close'].shift(1)

    df.dropna(subset=config['features'], inplace=True)

    X = df[config['features']]
    y = df[config['target_column']]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, shuffle=False, test_size=config["test_size"]
    )

    input_example = X_train.iloc[[0]]
    signature = infer_signature(X_train, y_train)

    with mlflow.start_run() as run:
        model = LinearRegression()
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        mse = mean_squared_error(y_test, preds)
        rmse = np.sqrt(mse)

        print(f"✅ RMSE: {rmse:.2f}")

        model_accepted = rmse < config.get("rmse_threshold", 7)

        

        try: 
            mlflow.sklearn.log_model(
                sk_model=model,
                artifact_path="faang_model",  
                registered_model_name="FAANG-Model",
                input_example=input_example,
                signature=signature
            )

            mlflow.log_metric("rmse", rmse)
        except Exception as e:
            print(f"Error logging model to MLflow: {e}")
            sys.exit(1)

        return {
            "rmse": rmse,
            "run_id": run.info.run_id,
            "experiment_id": run.info.experiment_id,
            "model_accepted": model_accepted
        }

if __name__ == "__main__":
    config_path = sys.argv[1] if len(sys.argv) > 1 else "/home/src/configs/train_config.yaml"
    train_model(config_path)