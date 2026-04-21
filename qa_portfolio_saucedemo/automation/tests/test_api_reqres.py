import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("REQRES_API_KEY")


def get_headers():
    assert API_KEY, "API key not found in .env"
    return {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }


def test_get_users():
    response = requests.get(
        f"{BASE_URL}/users?page=2",
        headers=get_headers()
    )

    assert response.status_code == 200

    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)


def test_create_user():
    payload = {
        "name": "Prajwal",
        "job": "QA"
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=payload,
        headers=get_headers()
    )

    assert response.status_code in [200, 201]

    data = response.json()
    assert data["name"] == "Prajwal"
    assert data["job"] == "QA"


def test_invalid_endpoint():
    response = requests.get(
        f"{BASE_URL}/unknown/999",
        headers=get_headers()
    )

    assert response.status_code == 404