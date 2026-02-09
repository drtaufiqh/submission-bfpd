import pytest
from unittest.mock import patch, Mock
from utils.extract import extract_data

BASE_URL = "https://fashion-studio.dicoding.dev/"

def test_extract_data_return_type():
    data = extract_data(BASE_URL, start_page=1, delay=0)
    assert isinstance(data, list)

def test_extract_data_structure():
    data = extract_data(BASE_URL, start_page=1, delay=0)

    assert len(data) > 0
    product = data[0]

    expected_keys = {
        "Title", "Price", "Rating",
        "Colors", "Size", "Gender", "Timestamp"
    }

    assert expected_keys.issubset(product.keys())

@patch("utils.extract.requests.session")
def test_extract_data_with_mocked_request(mock_session):
    # mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b"""
    <html>
        <body>
            <div class="product">
                <h3 class="title">Mock Product</h3>
                <span class="price">$100.00</span>
                <span class="rating">4.5</span>
            </div>
        </body>
    </html>
    """

    # mock session.get()
    mock_session.return_value.get.return_value = mock_response

    data = extract_data(BASE_URL, start_page=1, delay=0)

    assert isinstance(data, list)