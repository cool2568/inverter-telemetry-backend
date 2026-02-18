from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.inverter import Inverter

class InverterRepository:

    @staticmethod
    async def create(db:AsyncSession,inverter:Inverter)->Inverter:
        db.add(inverter)
        await db.commit()
        await db.refresh(inverter)
        return inverter
    
    @staticmethod
    async def get_by_user(db:AsyncSession,user_id:int):
        result= await db.excute(
            select(Inverter).where(Inverter.user_id==user_id)
        )
        return result.scalars().all()
    