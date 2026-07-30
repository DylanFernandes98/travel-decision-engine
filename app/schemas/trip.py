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