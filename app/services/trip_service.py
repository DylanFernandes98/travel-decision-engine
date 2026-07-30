from sqlmodel import Session
from app.models.trip import Trip
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

def create_trip(trip_data: TripCreate, session: Session) -> Trip:
    # Convert the validated API schema into a database model
    trip = Trip.model_validate(trip_data)

    session.add(trip)                   # Add new trip to current database session
    session.commit()                    # Save the new row to SQLite
    session.refresh(trip)               # Reload the trip from the database (retrive ID)

    return trip

def delete_trip(trip_id: int):
    # Find and remove a trip by ID
    for trip in trips:
        if trip["id"] == trip_id:
            deleted_trip = trip
            trips.remove(trip)
            return deleted_trip
    raise HTTPException(status_code=404, detail=f"Trip with ID: {trip_id} not found")