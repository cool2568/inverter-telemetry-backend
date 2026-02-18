from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime

from app.models.inverter import Inverter
from app.models.telemetry import Telemetry
from app.repositories.device_repo import DeviceRepository
from app.repositories.telemetry_repo import TelemetryRepository
from app.utils.energy import calculate_energy_kwh


class TelemetryService:

    @staticmethod
    async def ingest_from_mqtt(
        db:AsyncSession,
        device_uid:str,
        payload:dict

    ):
        device=await DeviceRepository.get_by_uid(db,device_uid)
        if not device:
            raise HTTPException(404,"Unknow device")
        
        res=await db.excute(
            select(Inverter).where(Inverter.device_id==device.id)
        )
        inverter=res.scaler_one_or_none()
        if not inverter:
            raise HTTPException(400,"Device not linked to inverter")
        

        grid_voltage=float(payload['VG'])
        grid_current=float