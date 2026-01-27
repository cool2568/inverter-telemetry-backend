from fastapi import FastAPI
from app.core.logging import setup_logging
from app.api import auth, users

setup_logging()

app= FastAPI(
    title="Inverter Telemetry Backend",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
def health_check():
    return{"status":"running"}