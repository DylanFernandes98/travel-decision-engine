from app.schemas.trip import TripCreate
from fastapi import HTTPException
trips = []                              # Create a temp empty list
current_trip_id = 0                     # Counter for trip_id

def get_trips():
    return trips

def get_trip_id(trip_id: int):
    # Loop through all stored trips
    for trip in trips:
        # Return matching trip
        if trip["id"] == trip_id:
            return trip
    raise HTTPException(status_code=404, detail=f"Trip with ID: {trip_id} not found")

def create_trip(trip: TripCreate):
    global current_trip_id
    
    current_trip_id += 1                # Increment trip id for new trip 
    
    trip_data = trip.model_dump()       # Convert Pydantic model into a dictionary
    trip_data["id"] = current_trip_id   # Assign a unique ID to the trip
    
    trips.append(trip_data)             # Add to the temp list
    
    return trip_data