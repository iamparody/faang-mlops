import sys
import os
import pandas as pd
from datetime import datetime

sys.path.insert(0, '/home/src')

from training.train import train_model

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    """
    Save cleaned data and run training. Optionally register model if metrics are good.
    """
    # 1. Save incoming data to CSV
    csv_path = '/home/src/data/faang_clean.csv'
    data.to_csv(csv_path, index=False)

    # 2. Point to your training config
    config_path = '/home/src/configs/train_config.yaml'

    # 3. Run model training
    result = train_model(config_path)  # Make sure this returns dict: {rmse, run_id, etc.}

    # 4. Optional: register model if RMSE < threshold
    rmse = result.get('rmse', None)
    if rmse is not None and rmse < 7:
        result['model_accepted'] = True
        # Optionally register the model to MLflow registry here
        # e.g., mlflow.register_model(...)

    else:
        result['model_accepted'] = False

    return result

@test
def test_output(output, *args) -> None:
    assert 'rmse' in output, 'No RMSE returned'
