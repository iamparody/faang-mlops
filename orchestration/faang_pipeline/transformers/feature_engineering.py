if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    """
    Adds Prev_Close as a lag feature and drops rows with missing values.
    """
    data['Prev_Close'] = data.groupby('Ticker')['Close'].shift(1)
    data = data.dropna(subset=['Prev_Close'])
    return data

@test
def test_output(output, *args) -> None:
    """
    Check that feature was added and nulls were removed.
    """
    assert output is not None, 'Output is None'
    assert 'Prev_Close' in output.columns, 'Prev_Close column missing'
    assert output['Prev_Close'].isnull().sum() == 0, 'Prev_Close still has nulls'
