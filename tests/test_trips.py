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
    response = client.get("/trips")         # Send a GET request to /trips endpoint
    assert response.status_code == 200      # Check request was successful
    assert response.json() == []            # Check endpoint returns empty list

def test_create_trip(sample_trip_data):
    response = client.post("/trips", json=sample_trip_data) # Create a new trip

    trip_id = response.json()["id"]

    assert response.status_code == 200      # Check request was successful
    
    response_json = response.json()

    # Check trip data was stored correctly
    assert response_json["destination"] == "Thailand"
    assert response_json["duration_days"] == 14
    assert response_json["people_count"] == 2
    assert response_json["annual_leave_days"] == 10
    assert response_json["id"] == trip_id   # Check a trip ID was generated

def test_get_trip_id(sample_trip_data):
    create_response = client.post("/trips", json=sample_trip_data) # Create a trip to retrieve

    trip_id = create_response.json()["id"] 
    
    response = client.get(f"/trips/{trip_id}") # Retrieve the trip using its ID

    assert response.status_code == 200      # Check request was successful
    
    response_json = response.json()

    # Check retrieved trip matches created trip
    assert response_json["destination"] == "Thailand"
    assert response_json["duration_days"] == 14
    assert response_json["people_count"] == 2
    assert response_json["annual_leave_days"] == 10
    assert response_json["id"] == trip_id