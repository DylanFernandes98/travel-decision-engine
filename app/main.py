from fastapi import FastAPI
from app.routes.trips import router
# Imports the router from the trips module

app = FastAPI(title="Travel Decision Engine")

app.include_router(router)
# Registers the trips router with the main app

@app.get("/")
# Defines a GET endpoint for the root URL (/)
def root():
    return {
        "message": "Travel Decision Engine API"
    }