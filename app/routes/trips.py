"""Defines the FastAPI endpoints for trip operations."""

from typing import Annotated
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.schemas.trip import TripCreate, TripResponse, TripUpdate
from app.services import trip_service

# Creates a router object to group related endpoints
router = APIRouter()

# GET endpoint to retrieve all trips
@router.get("/trips", response_model=list[TripResponse])
async def get_trips(session: Annotated[Session, Depends(get_session)]):
    return trip_service.get_trips(session)

# GET endpoint to retrieve a specific trip by ID
@router.get("/trips/{trip_id}", response_model=TripResponse)
async def get_trip_id(trip_id: int, session: Annotated[Session, Depends(get_session)]):
    return trip_service.get_trip_id(trip_id, session)
    
# POST endpoint to create a new trip
@router.post("/trips", response_model=TripResponse)
async def create_trip(trip: TripCreate, session: Annotated[Session, Depends(get_session)]):
    return trip_service.create_trip(trip, session)

# PATCH endpoint to update a trip
@router.patch("/trips/{trip_id}", response_model=TripResponse)
async def update_trip(trip_id: int, trip: TripUpdate, session: Annotated[Session, Depends(get_session)]):
    return trip_service.update_trip(trip_id, trip, session)

# DELETE endpoint to delete a specific trip by ID
@router.delete("/trips/{trip_id}", response_model=TripResponse)
async def delete_trip_by_id(trip_id: int, session: Annotated[Session, Depends(get_session)]):
    return trip_service.delete_trip(trip_id, session)