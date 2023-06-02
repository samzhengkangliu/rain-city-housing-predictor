import json
from flask import Flask
import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    client = app.test_client()
    yield client


def test_perform_analysis(client):
    # Assume we have some test data in the database
    # Call the analysis route and assert the response
    response = client.get("/api/analysis")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "analysis_results" in data
    assert "summary" in data
