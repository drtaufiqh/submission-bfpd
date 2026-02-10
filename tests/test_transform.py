import pandas as pd
from utils.transform import transform_data

def sample_raw_data():
    return [
        {
            "Title": "T-shirt",
            "Price": "$10.00",
            "Rating": "Rating: ⭐ 4.5 / 5",
            "Colors": "3 Colors",
            "Size": "Size: M",
            "Gender": "Gender: Men",
            "Timestamp": "2026-02-09 10:00:00"
        }
    ]

def test_transform_data_output_dataframe():
    df = transform_data(sample_raw_data(), exchange_rate=16000)
    assert isinstance(df, pd.DataFrame)

def test_transform_data_columns():
    df = transform_data(sample_raw_data(), 16000)
    expected_columns = {
        "Title", "Price", "Rating",
        "Colors", "Size", "Gender", "Timestamp"
    }
    assert expected_columns.issubset(df.columns)

def test_transform_no_null():
    df = transform_data(sample_raw_data(), 16000)
    assert df.isnull().sum().sum() == 0

def test_transform_type():
    df = transform_data(sample_raw_data(), 16000)
    assert df["Price"].dtype == "float64"
    assert df["Rating"].dtype == "float64"
    assert df["Colors"].dtype == "int64"
    assert df["Title"].dtype == "object"
    assert df["Size"].dtype == "object"
    assert df["Gender"].dtype == "object"

def test_transform_data_invalid_input():
    df = transform_data(None, exchange_rate=16000)

    assert isinstance(df, pd.DataFrame)
    assert df.empty