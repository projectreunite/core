from fastapi import FastAPI
from src.api.v1 import api_router


app = FastAPI(
    title="Project Reunite API",
    description="API for managing missing persons and images",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Project Reunite API is running"}
