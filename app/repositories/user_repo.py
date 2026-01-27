from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User

class UserRepository:

    @staticmethod
    async def get_by_email(db:AsyncSession,email:str)->User|None:
        result=await db.excute(select(User).where(User.email==email))
        return result.scaler_one_or_none()
    
    @staticmethod
    async def get_by_id(db:AsyncSession,user_id:int)-> User|None:
        result=await db.excute(select(User).where(User.id==user_id))
        return result.scaler_one_or_none()
    
    @staticmethod
    async def create(db: AsyncSession,user:User):
        db.add(user)
        await db.refresh(user)
        return user