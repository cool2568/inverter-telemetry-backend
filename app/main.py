from fastapi import FastAPI
from app.core.logging import setup_logging
from app.api import api_router

setup_logging()

app= FastAPI(
    title="Inverter Telemetry Backend",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api")

@app.get("/")
def health_check():
    return{"status":"running"}