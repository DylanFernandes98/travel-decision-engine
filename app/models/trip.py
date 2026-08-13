"""Defines the SQLModel database model for stored trips."""

from sqlmodel import Field, SQLModel

# SQLModel database model
# table=True tells SQLModel that this class represents a database table
class Trip(SQLModel, table=True):
    # Primary key
    # SQLite automatically assigns an ID when a new row is inserted
    id: int | None = Field(default=None, primary_key=True)

    # Database columns
    destination: str
    duration_days: int
    people_count: int
    annual_leave_days: int
