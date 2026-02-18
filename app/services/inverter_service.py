from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.inverter import Inverter
from app.repositories.inverter_repo import InverterRepository
from app.repositories.device_repo import DeviceRepository

class InverterService:

    @staticmethod
    async def create_inverter(
        db:AsyncSession,
        user_id:int,
        device_uid:str,
        name:str,
        model_number:str|None,
        manufacturer:str|None,
    ):
        device=await DeviceRepository.get_by_uid(db,device_uid)

        if not device:
            raise HTTPException(status_code=404,detail='Invalid device')
        
        if device.is_registered:
            raise HTTPException(status_code=400,detail='Device already registered')
        
        inverter=Inverter(
            user_id=user_id,
            device_id=device.id,
            name=name,
            serial_number=device.serial_number,
            model_number=model_number,
            manufacturer=manufacturer,
            created_by=user_id,
            updated_by=user_id
        )

        device.is_registered=True
        device.updated_by=user_id

        return await InverterRepository.create(db,inverter)
    
    @staticmethod
    async def list_user_inverters(db:AsyncSession,user_id:int):
        return await InverterRepository.get_by_user(db,user_id)