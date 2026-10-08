"""Contains the business logic and database operations for cost_items."""

from sqlmodel import Session, select
from app.models.cost_item import CostItem
from app.schemas.cost_item import CostItemCreate, CostItemUpdate
from app.services.trip_service import get_trip_id
from fastapi import HTTPException

def get_cost_items(trip_id: int, session: Session):
    # Verify the parent Trip exists
    get_trip_id(trip_id, session)

    # Build a query that selects every CostItem from the database where trip_id is equal
    statement = select(CostItem).where(CostItem.trip_id == trip_id)
    
    # Execute the query and return all matching rows
    cost_items = session.exec(statement).all()

    return cost_items

def get_cost_item_id(cost_item_id: int, session: Session):
    # Look up CostItem using its primary key
    cost_item = session.get(CostItem, cost_item_id)

    if cost_item is None:
        raise HTTPException(status_code=404, detail="Cost Item not found")

    return cost_item

def get_trip_cost_item(trip_id: int, cost_item_id: int, session: Session):
    # Retrieve the CostItem, raising 404 if it doesn't exist
    cost_item = get_cost_item_id(cost_item_id, session)

    # Check that the CostItem belongs to the requested Trip
    if trip_id != cost_item.trip_id:
        raise HTTPException(status_code=404, detail="Cost Item not found")

    return cost_item

def create_cost_item(trip_id: int, cost_item_data: CostItemCreate, session: Session):
    # Verify the parent Trip exists
    get_trip_id(trip_id, session)
    # Convert the validated API schema into a database model
    cost_item = CostItem.model_validate(
        cost_item_data,
        update={"trip_id": trip_id} 
    )
    
    session.add(cost_item)              # Add new cost_item to current database session
    session.commit()                    # Save the new row to SQLite
    session.refresh(cost_item)          # Reload the cost_item from the database (retrieve ID)
    
    return cost_item

def update_cost_item(trip_id: int, cost_item_id: int, cost_item_data: CostItemUpdate, session: Session):
    # Look up CostItem using its primary key
    cost_item = get_trip_cost_item(trip_id, cost_item_id, session)

    # Convert only the fields supplied in the PATCH request into a dict
    update_data = cost_item_data.model_dump(exclude_unset=True)

    # Update each supplied field on the existing CostItem
    for key, value in update_data.items():
        setattr(cost_item, key, value)

    session.commit()                    # Save the updated cost_item to SQLite
    session.refresh(cost_item)          # Reload the cost_item from the database

    return cost_item

def delete_cost_item(trip_id: int, cost_item_id: int, session: Session):
    # Look up CostItem by its primary key
    cost_item = get_trip_cost_item(trip_id, cost_item_id, session)

    session.delete(cost_item)           # Mark the cost_item for deletion
    session.commit()                    # Perm remove from database

    return cost_item