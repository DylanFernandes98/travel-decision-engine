import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
# Creates a test client for making requests to the API

@pytest.fixture
def sample_trip_data():
    # Reusable test data shared across multiple tests
    return {
        "destination": "Thailand", 
        "duration_days": 14,
        "people_count": 2,
        "annual_leave_days": 10,
    }

def test_get_trips():
    get_response = client.get("/trips")         # Send a GET request to /trips endpoint
    assert get_response.status_code == 200      # Check request was successful
    assert get_response.json() == []            # Check endpoint returns empty list

def test_create_trip(sample_trip_data):
    create_response = client.post("/trips", json=sample_trip_data) # Create a new trip

    trip_id = create_response.json()["id"]

    assert create_response.status_code == 200      # Check request was successful
    
    response_json = create_response.json()

    # Check trip data was stored correctly
    assert response_json["destination"] == "Thailand"
    assert response_json["duration_days"] == 14
    assert response_json["people_count"] == 2
    assert response_json["annual_leave_days"] == 10
    assert response_json["id"] == trip_id   # Check a trip ID was generated

def test_get_trip_id(sample_trip_data):
    create_response = client.post("/trips", json=sample_trip_data) # Create a trip to retrieve

    trip_id = create_response.json()["id"] 
    
    get_response = client.get(f"/trips/{trip_id}") # Retrieve the trip using its ID

    assert get_response.status_code == 200      # Check request was successful
    
    response_json = get_response.json()

    # Check retrieved trip matches created trip
    assert response_json["destination"] == "Thailand"
    assert response_json["duration_days"] == 14
    assert response_json["people_count"] == 2
    assert response_json["annual_leave_days"] == 10
    assert response_json["id"] == trip_id

def test_delete_trip(sample_trip_data):
    create_response = client.post("/trips", json=sample_trip_data)

    trip_id = create_response.json()["id"]

    delete_response = client.delete(f"/trips/{trip_id}")

    assert delete_response.status_code == 200

    response_json = delete_response.json()

    # Check retrieved trip matches created trip
    assert response_json["destination"] == "Thailand"
    assert response_json["duration_days"] == 14
    assert response_json["people_count"] == 2
    assert response_json["annual_leave_days"] == 10
    assert response_json["id"] == trip_id

def test_deleted_trip_returns_404(sample_trip_data):
    create_response = client.post("/trips", json=sample_trip_data)

    trip_id = create_response.json()["id"]

    delete_response = client.delete(f"/trips/{trip_id}")

    get_response = client.get(f"/trips/{trip_id}")

    assert get_response.status_code == 404
    assert get_response.json()["detail"] == f"Trip with ID: {trip_id} not found"