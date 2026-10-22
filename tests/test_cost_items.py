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

def test_get_cost_items(sample_trip_id, sample_cost_item_data):
    create_response = client.post(f"/trips/{sample_trip_id}/cost-items", json=sample_cost_item_data)

    get_response = client.get(f"/trips/{sample_trip_id}/cost-items")

    assert get_response.status_code == 200

    response_json = get_response.json()

    assert len(response_json) == 1
    assert response_json[0]["name"] == "Hotel"

def test_get_cost_items_id(sample_trip_id, sample_cost_item_data):
    create_response = client.post(f"/trips/{sample_trip_id}/cost-items", json=sample_cost_item_data)

    cost_id = create_response.json()["id"]
    
    get_response = client.get(f"/trips/{sample_trip_id}/cost-items/{cost_id}")
    
    assert get_response.status_code == 200
    
    response_json = get_response.json()

    assert response_json["id"] == cost_id

def test_update_cost_items(sample_trip_id, sample_cost_item_data):
    create_response = client.post(f"/trips/{sample_trip_id}/cost-items", json=sample_cost_item_data)

    cost_id = create_response.json()["id"]

    update_response = client.patch(f"/trips/{sample_trip_id}/cost-items/{cost_id}", json={"unit_cost": "150.00"})

    assert update_response.status_code == 200

    update_json = update_response.json()

    assert update_json["name"] == "Hotel"
    assert update_json["unit_cost"] == "150.00"
    assert update_json["category"] == "accommodation"
    assert update_json["time_basis"] == "per_night"
    assert update_json["traveller_basis"] == "shared"
    assert update_json["duration_override"] is None

def test_update_cost_items_returns_404():
    update_response = client.patch("/trips/999/cost-items/999", json={"unit_cost": "150.00"})

    assert update_response.status_code == 404
    assert update_response.json()["detail"] == "Cost Item not found"

def test_delete_cost_items(sample_trip_id, sample_cost_item_data):
    create_response = client.post(f"/trips/{sample_trip_id}/cost-items", json=sample_cost_item_data)

    cost_id = create_response.json()["id"]

    delete_response = client.delete(f"/trips/{sample_trip_id}/cost-items/{cost_id}")

    assert delete_response.status_code == 200

    response_json = delete_response.json()

    assert response_json["name"] == "Hotel"
    assert response_json["unit_cost"] == "100.00"
    assert response_json["category"] == "accommodation"
    assert response_json["time_basis"] == "per_night"
    assert response_json["traveller_basis"] == "shared"
    assert response_json["duration_override"] is None
    assert response_json["id"] == cost_id

    # Verify the deleted CostItem can no longer be retrieved
    get_response = client.get(f"/trips/{sample_trip_id}/cost-items/{cost_id}")

    assert get_response.status_code == 404
    assert get_response.json()["detail"] == "Cost Item not found"

def test_deleted_trip_returns_404(sample_trip_id, sample_cost_item_data):
    create_response = client.post(f"/trips/{sample_trip_id}/cost-items", json=sample_cost_item_data)

    cost_id = create_response.json()["id"]

    delete_response = client.delete(f"/trips/{sample_trip_id}/cost-items/{cost_id}")

    get_response = client.get(f"/trips/{sample_trip_id}/cost-items{cost_id}")

    assert get_response.status_code == 404
    assert get_response.json()["detail"] == "Not Found"

def test_create_cost_item_rejects_negative_cost(sample_trip_id, sample_cost_item_data):
    sample_cost_item_data["unit_cost"] = "-50.00"

    create_response = client.post(f"/trips/{sample_trip_id}/cost-items", json=sample_cost_item_data)

    assert create_response.status_code == 422