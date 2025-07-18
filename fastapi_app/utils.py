import mlflow.pyfunc
import os

def load_model(model_name: str):
    """
    Load the latest version of a registered model from the MLflow model registry.
    Assumes MLflow tracking URI is set via environment variable or default.
    """
    try:
        tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000")
        mlflow.set_tracking_uri(tracking_uri)

        # 🚨 Change from model_name to full registry URI format
        model_uri = f"models:/{model_name}/latest"
        print(f"🔁 Loading model from URI: {model_uri}")
        
        model = mlflow.pyfunc.load_model(model_uri)
        print("✅ Model loaded successfully.")
        return model

    except Exception as e:
        print(f"❌ Failed to load model: {e}")
        raise e
