"""Defines Pydantic schemas for validating trip API data."""

from pydantic import BaseModel, Field

# Base schema for validating trip data sent to the API
# Schemas define the shape of request and response data
class TripCreate(BaseModel):
    destination: str
    duration_days: int
    duration_nights: int
    people_count: int = Field(ge=1, le=2)

# Response schema returned to the client
# Inherits all fields from TripCreate and adds the generated database ID
class TripResponse(TripCreate):
    id: int

# Schema for partially updating existing trip data
class TripUpdate(BaseModel):
    destination: str | None = None      # Destination can contain str or None; defaults to None
    duration_days: int | None = None
    duration_nights: int | None = None
    people_count: int | None = Field(default=None, ge=1, le=2)