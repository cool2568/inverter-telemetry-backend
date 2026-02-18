from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.device import Device

class DeviceRepository:

    @staticmethod
    async def get_by_uid(db:AsyncSession,device_uid:str):
        result = await db.execute(
            select(Device).where(Device.device_uid == device_uid)
        )
        return result.scalar_one_or_none()