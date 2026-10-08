"""Defines the FastAPI endpoints for cost_items operations."""

from typing import Annotated
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.schemas.cost_item import CostItemCreate, CostItemResponse, CostItemUpdate
from app.services import cost_item_service

# Creates a router object to group related endpoints
router = APIRouter(
    prefix="/trips/{trip_id}/cost-items",
    tags=["Cost Items"]
)

# GET endpoint to retrieve all cost_items
@router.get("", response_model=list[CostItemResponse])
async def get_cost_items(
    trip_id: int, 
    session: Annotated[Session, Depends(get_session)]
):
    return cost_item_service.get_cost_items(trip_id, session)

# GET endpoint to retrieve a specific cost_item by ID
@router.get("/{cost_item_id}", response_model=CostItemResponse)
async def get_cost_item_id(
    trip_id: int, 
    cost_item_id: int, 
    session: Annotated[Session, Depends(get_session)]
):
    return cost_item_service.get_trip_cost_item(trip_id, cost_item_id, session)
    
# POST endpoint to create a new cost_item
@router.post("", response_model=CostItemResponse)
async def create_cost_item(
    trip_id: int, 
    cost_item: CostItemCreate, 
    session: Annotated[Session, Depends(get_session)]
):
    return cost_item_service.create_cost_item(trip_id, cost_item, session)

# PATCH endpoint to update a cost_item
@router.patch("/{cost_item_id}", response_model=CostItemResponse)
async def update_cost_item(
    trip_id: int, 
    cost_item_id: int, 
    cost_item: CostItemUpdate, 
    session: Annotated[Session, Depends(get_session)]
):
    return cost_item_service.update_cost_item(trip_id, cost_item_id, cost_item, session)

# DELETE endpoint to delete a specific cost_item by ID
@router.delete("/{cost_item_id}", response_model=CostItemResponse)
async def delete_cost_item_by_id(
    trip_id: int, 
    cost_item_id: int, 
    session: Annotated[Session, Depends(get_session)]
):
    return cost_item_service.delete_cost_item(trip_id, cost_item_id, session)