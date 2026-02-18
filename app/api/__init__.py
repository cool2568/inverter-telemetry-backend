from fastapi import APIRouter
from app.api import auth,users,inverters,telemetry

api_router = APIRouter()

api_router.include_router(auth.router,prefix="/auth")
api_router.include_router(users.router, prefix="/users")
api_router.include_router(inverters.router, prefix="/inverters")
# api_router.include_router(telemetry.router, prefix="/telemetry")