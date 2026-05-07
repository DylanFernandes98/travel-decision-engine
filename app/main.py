from fastapi import FastAPI

app = FastAPI(title="Travel Decision Engine")


@app.get("/")
def root():
    return {
        "message": "Travel Decision Engine API"
    }