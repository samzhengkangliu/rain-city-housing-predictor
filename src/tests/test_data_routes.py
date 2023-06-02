import json
from flask import Flask
import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    client = app.test_client()
    yield client


def test_get_data(client):
    response = client.get("/api/data")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)


def test_post_data(client):
    payload = {"beds": 4, "baths": 2.5, "price": 800000, "zipcode": 98002}
    response = client.post("/api/data", json=payload)
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data["message"] == "Data created successfully"


def test_invalid_data(client):
    payload = {
        "beds": 4,
        "baths": "2.5",  # invalid input
        "price": 800000,
        "zipcode": 98002,
    }
    response = client.post("/api/data", json=payload)
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["message"] == "Invalid data format"
