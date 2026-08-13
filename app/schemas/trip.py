"""Defines Pydantic schemas for validating trip API data."""

from pydantic import BaseModel

# Base schema for validating trip data sent to the API
# Schemas define the shape of request and response data
class TripCreate(BaseModel):
    destination: str
    duration_days: int
    people_count: int
    annual_leave_days: int


# Response schema returned to the client
# Inherits all fields from TripCreate and adds the generated database ID
class TripResponse(TripCreate):
    id: int

# Schema for partially updating existing trip data
class TripUpdate(BaseModel):
    destination: str | None = None      # Destination can contain str or None; defaults to None
    duration_days: int | None = None
    people_count: int | None = None
    annual_leave_days: int | None = None