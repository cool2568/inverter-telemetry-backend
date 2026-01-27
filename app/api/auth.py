from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from app.services.auth_service import AuthService
from app.core.database import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register(
    payload: RegisterRequest,
    db: AsyncSession = Depends(get_db)
):
    return await AuthService.register(db, payload.email, payload.password)

@router.post("/login", response_model=TokenResponse)
async def login(
    payload: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    return await AuthService.login(db, payload.email, payload.password)