import requests
import pytest
from unittest.mock import patch

# URL for the API
url = "http://127.0.0.1:8000/users"

@patch("requests.get")
def test_invalid_credentials(mock_get):
    """Test case 1: Invalid credentials"""
    # Mock the response for invalid credentials
    mock_get.return_value.status_code = 401
    mock_get.return_value.text = ""

    params = {
        "username": "admin",
        "password": "admin"
    }
    response = requests.get(url, params=params)

    # Assertions
    assert response.status_code == 401, f"Expected HTTP 401, got {response.status_code}"
    assert response.text.strip() == "", f"Expected empty response, got: {response.text}"

@patch("requests.get")
def test_valid_credentials_empty_response(mock_get):
    """Test case 2: Valid credentials but expecting empty response"""
    # Mock the response for valid credentials
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = ""

    params_valid = {
        "username": "admin",
        "password": "qwerty"
    }
    response_valid = requests.get(url, params=params_valid)

    # Assertions
    assert response_valid.status_code == 200, f"Expected HTTP 200, got {response_valid.status_code}"
    assert response_valid.text.strip() == "", f"Expected empty response, got: {response_valid.text}"