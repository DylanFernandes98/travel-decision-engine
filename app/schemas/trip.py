from pydantic import BaseModel

class TripCreate(BaseModel):
    destination: str
    duration_days: int
    people_count: int
    annual_leave_days: int