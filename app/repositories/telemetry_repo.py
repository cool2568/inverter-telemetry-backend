from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from app.models.telemetry import Telemetry

class TelemetryRepository:

    @staticmethod
    async def insert(db: AsyncSession, telemetry: Telemetry):
        db.add(telemetry)
        await db.commit()
