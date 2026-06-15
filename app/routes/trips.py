from fastapi import APIRouter
from app.schemas.trip import TripCreate, TripResponse
from app.services import trip_service

router = APIRouter()
# Creates a router object to group related endpoints

@router.get("/trips", response_model=list[TripResponse])
# GET endpoint to retrieve all trips
async def get_trips():
    return trip_service.get_trips()

@router.get("/trips/{trip_id}", response_model=TripResponse)
# GET endpoint to retrieve a specific trip by ID
async def get_trip_id(trip_id: int):
    return trip_service.get_trip_id(trip_id)
    
@router.post("/trips", response_model=TripResponse)
# POST endpoint to create a new trip
async def create_trip(trip: TripCreate):
    return trip_service.create_trip(trip)