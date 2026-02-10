import pandas as pd
from unittest.mock import patch, MagicMock
from utils.load import load_data, load_to_postgre, load_to_csv, load_to_spreadsheets

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

@patch("utils.load.build")
def test_load_to_spreadsheets_success(mock_build):
    mock_service = MagicMock()
    mock_sheet = MagicMock()

    mock_build.return_value = mock_service
    mock_service.spreadsheets.return_value = mock_sheet

    df = sample_dataframe()
    load_to_spreadsheets(df)

    mock_build.assert_called_once()

    assert mock_sheet.values().update.called

def test_load_to_postgre_error_printed(capsys):
    df = sample_dataframe()
    # create_engine dibuat gagal
    with patch("utils.load.create_engine", side_effect=Exception("DB error")):
        load_to_postgre(df, "postgresql://invalid")

    captured = capsys.readouterr()

    assert "Gagal menyimpan ke PostgreSQL" in captured.out
    assert "DB error" in captured.out

def test_load_to_spreadsheets_error_printed(capsys):
    df = sample_dataframe()
    # build() Google API dibuat gagal
    with patch("utils.load.build", side_effect=Exception("Google API error")):
        load_to_spreadsheets(df)

    captured = capsys.readouterr()

    assert "Gagal menyimpan ke Google Sheets" in captured.out
    assert "Google API error" in captured.out

def test_load_data_error_printed_csv(capsys):
    df = sample_dataframe()
    # load_to_csv dibuat error
    with patch("utils.load.load_to_csv", side_effect=Exception("CSV error")), \
         patch("utils.load.load_to_spreadsheets") as mock_sheet, \
         patch("utils.load.load_to_postgre") as mock_pg:

        load_data(df, "dummy.csv", "postgresql://dummy")

    captured = capsys.readouterr()

    assert "Terjadi kesalahan pada proses load" in captured.out
    assert "CSV error" in captured.out

    mock_sheet.assert_not_called()
    mock_pg.assert_not_called()

def test_load_data_error_printed_sheet(capsys):
    df = sample_dataframe()
    # load_to_spreadsheets dibuat error
    with patch("utils.load.load_to_spreadsheets", side_effect=Exception("Spreadsheets error")), \
         patch("utils.load.load_to_postgre") as mock_pg:

        load_data(df, "dummy.csv", "postgresql://dummy")

    captured = capsys.readouterr()

    assert "Terjadi kesalahan pada proses load" in captured.out
    assert "Spreadsheets error" in captured.out

    mock_pg.assert_not_called()

def test_load_data_error_printed_pg(capsys):
    df = sample_dataframe()
    # load_to_postgre dibuat error
    with patch("utils.load.load_to_postgre", side_effect=Exception("PostgreSQL error")):

        load_data(df, "dummy.csv", "postgresql://dummy")

    captured = capsys.readouterr()

    assert "Terjadi kesalahan pada proses load" in captured.out
    assert "PostgreSQL error" in captured.out