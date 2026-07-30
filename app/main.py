from fastapi import FastAPI
# Imports the router from the trips module
from app.routes.trips import router
# Imports the database
from app.core.database import create_db_and_tables

app = FastAPI(title="Travel Decision Engine")

# Creates any missing tables
create_db_and_tables()

# Registers the trips router with the main app
app.include_router(router)

# Defines a GET endpoint for the root URL (/)
@app.get("/")
def root():
    return {
        "message": "Travel Decision Engine API"
    }