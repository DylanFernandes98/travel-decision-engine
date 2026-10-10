"""Tests the CostItem API endpoints and their expected behaviour."""

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel

from app.main import app
from app.core.database import engine

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_database():
    # Reset the database before every test
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

    yield


@pytest.fixture
def sample_trip_id():
    # Create a Trip for CostItems to belong to
    trip_data = {
        "destination": "Thailand",
        "duration_days": 14,
        "duration_nights": 13,
        "people_count": 2,
    }

    response = client.post("/trips", json=trip_data)

    assert response.status_code == 200
    return response.json()["id"]


@pytest.fixture
def sample_cost_item_data():
    return {
        "name": "Hotel",
        "unit_cost": "100.00",
        "category": "accommodation",
        "time_basis": "per_night",
        "traveller_basis": "shared",
        "duration_override": None,
    }

def test_create_cost_item(sample_trip_id, sample_cost_item_data):
    create_response = client.post(f"/trips/{sample_trip_id}/cost-items", json=sample_cost_item_data)

    assert create_response.status_code == 200

    response_json = create_response.json()

     # Check CostItem data was stored correctly
    assert response_json["name"] == "Hotel"
    assert response_json["unit_cost"] == "100.00"
    assert response_json["category"] == "accommodation"
    assert response_json["time_basis"] == "per_night"
    assert response_json["traveller_basis"] == "shared"
    assert response_json["duration_override"] is None

    assert isinstance(response_json["id"], int)
    assert response_json["trip_id"] == sample_trip_id