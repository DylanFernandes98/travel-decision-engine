"""Defines the SQLModel database model for stored cost_items."""

from app.models.enums import CostCategory, TimeBasis, TravellerBasis
from sqlmodel import Field, SQLModel
from decimal import Decimal

# SQLModel database model
# table=True tells SQLModel that this class represents a database table
class CostItem(SQLModel, table=True):
    # Primary key
    id: int | None = Field(default=None, primary_key=True)

    # Foreign key referencing the Trip table
    trip_id: int = Field(foreign_key="trip.id")

    # Database columns
    name: str
    unit_cost: Decimal = Field(ge=0, max_digits=10, decimal_places=2)
    category: CostCategory
    time_basis: TimeBasis
    traveller_basis: TravellerBasis
    duration_override: int | None = Field(default=None, ge=1)