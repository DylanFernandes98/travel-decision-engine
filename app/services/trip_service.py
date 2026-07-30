from sqlmodel import Session, select
from app.models.trip import Trip
from app.schemas.trip import TripCreate
from fastapi import HTTPException

def get_trips(session: Session):
    # Build a query that selects every Trip from the database
    statement = select(Trip)
    # Execute the query and return all matching rows
    trips = session.exec(statement).all()

    return trips

def get_trip_id(trip_id: int, session: Session):
    # Look up Trip using its primary key
    trip = session.get(Trip, trip_id)

    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")

    return trip

def create_trip(trip_data: TripCreate, session: Session) -> Trip:
    # Convert the validated API schema into a database model
    trip = Trip.model_validate(trip_data)

    session.add(trip)                   # Add new trip to current database session
    session.commit()                    # Save the new row to SQLite
    session.refresh(trip)               # Reload the trip from the database (retrive ID)

    return trip

def delete_trip(trip_id: int, session: Session):
    # Look up Trip by its primary key
    trip = session.get(Trip, trip_id)

    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")

    session.delete(trip)                # Mark the trip for deletion
    session.commit()                    # Perm remove from database

    return trip