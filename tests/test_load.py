import pandas as pd
from utils.load import load_to_csv

def sample_dataframe():
    return pd.DataFrame({
        "Title": ["T-shirt"],
        "Price": [160000],
        "Rating": [4.5],
        "Colors": [3],
        "Size": ["M"],
        "Gender": ["Men"],
        "Timestamp": ["2026-02-09 10:00:00"]
    })

def test_load_to_csv(tmp_path):
    df = sample_dataframe()
    file_path = tmp_path / "test.csv"

    load_to_csv(df, file_path)

    assert file_path.exists()