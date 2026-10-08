"""Defines Pydantic schemas for validating cost_item API data."""

from app.models.enums import CostCategory, TimeBasis, TravellerBasis
from pydantic import BaseModel, Field, model_validator
from decimal import Decimal

# Base schema for validating cost_item data sent to the API
# Schemas define the shape of request and response data
class CostItemCreate(BaseModel):
    name: str
    unit_cost: Decimal = Field(ge=0, max_digits=10, decimal_places=2)
    category: CostCategory
    time_basis: TimeBasis
    traveller_basis: TravellerBasis
    duration_override: int | None = Field(default=None, ge=1)

# Response schema returned to the client
# Inherits all fields from CostItemCreate and adds the generated database ID
class CostItemResponse(CostItemCreate):
    id: int
    trip_id: int

# Schema for partially updating existing cost_item data
class CostItemUpdate(BaseModel):
    name: str | None = None
    unit_cost: Decimal | None = Field(default=None, ge=0, max_digits=10, decimal_places=2)
    category: CostCategory | None = None
    time_basis: TimeBasis | None = None
    traveller_basis: TravellerBasis | None = None
    duration_override: int | None = Field(default=None, ge=1)

    # Runs custom validation after Pydantic has validated the individual fields
    @model_validator(mode="after")
    def validate_update(self):
        # Loop through only the fields explicitly provided in the PATCH request
        for field_name in self.model_fields_set:
            value = getattr(self, field_name)
            # Reject explicit null values, except when clearing duration_override
            if value is None and field_name != "duration_override":
                raise ValueError("Field cannot be null")
        return self
