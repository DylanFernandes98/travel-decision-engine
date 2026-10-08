"""Creates and configures the FastAPI application."""

from fastapi import FastAPI
# Imports the routers
from app.routes.trips import router as trips_router
from app.routes.cost_items import router as cost_items_router
# Imports the database
from app.core.database import create_db_and_tables

app = FastAPI(title="Travel Decision Engine")

# Creates any missing tables
create_db_and_tables()

# Registers both routers with the main app
app.include_router(trips_router)
app.include_router(cost_items_router)

# Defines a GET endpoint for the root URL (/)
@app.get("/")
def root():
    return {
        "message": "Travel Decision Engine API"
    }