import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_file(*args, **kwargs):
    """
    Loads the cleaned FAANG data CSV.
    """
    filepath = '/home/src/data/faang_clean.csv' 
    df = pd.read_csv(filepath)
    return df

@test
def test_output(output, *args) -> None:
    """
    Basic check to make sure data is loaded.
    """
    assert output is not None, 'Dataframe is None'
    assert not output.empty, 'Dataframe is empty'
    assert 'Close' in output.columns, 'Missing expected column: Close'
