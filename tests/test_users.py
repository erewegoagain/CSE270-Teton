import requests
import pytest

# URL for the API
url = "http://127.0.0.1:8000/users"

def test_invalid_credentials():
    """Test case 1: Invalid credentials"""
    params = {
        "username": "admin",
        "password": "admin"
    }
    response = requests.get(url, params=params)
    assert response.status_code == 401, f"Expected HTTP 401, got {response.status_code}"
    assert response.text.strip() == "", f"Expected empty response, got: {response.text}"

def test_valid_credentials_empty_response():
    """Test case 2: Valid credentials but expecting empty response"""
    params_valid = {
        "username": "admin",
        "password": "qwerty"
    }
    response_valid = requests.get(url, params=params_valid)
    assert response_valid.status_code == 200, f"Expected HTTP 200, got {response_valid.status_code}"
    assert response_valid.text.strip() == "", f"Expected empty response, got: {response_valid.text}"