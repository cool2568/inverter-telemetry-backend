from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repo import UserRepository
from app.models.user import User
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

class AuthService:

    @staticmethod
    async def register(db: AsyncSession, email: str, password: str):
        existing = await UserRepository.get_by_email(db, email)
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")

        user = User(
            email=email,
            hashed_password=hash_password(password),
            created_by=None,      # system action
            updated_by=None
        )

        await UserRepository.create(db, user)
        return {"message": "User registered successfully"}
    
    @staticmethod
    async def  login(db:AsyncSession,email:str,password:str):
        user=await UserRepository.get_by_email(db,email)
        if not user or not verify_password(password,user.hashed_password):
            raise HTTPException(status_code=401,detail="Invalid Credentials")
        
        token=create_access_token(user.id)
        return{"access_token":token,"token_type":"bearer"}