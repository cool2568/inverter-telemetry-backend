from sqlalchemy import Column,Integer,Float,Boolean,DateTime,ForeignKey,Index
from sqlalchemy import func
from app.models.base import Base

class Telemetry(Base):
    __tablename__="telemetry"

    id=Column(Integer,primary_key=True)
    device_id=Column(Integer,ForeignKey("devices.id"),nullable=False,index=True)
    inverter_id=Column(Integer,ForeignKey("inverters.id"),nullable=False,index=True)

    timestamp=Column(DateTime(timezone=True),nullable=False,index=True)

    voltage=Column(Float,nullable=False)
    current=Column(Float,nullable=False)
    power=Column(Float,nullable=False)
    energy_kwh=Column(Float,nullable=False)
    temperature=Column(Float)
    grid_connected=Column(Boolean,default=True)

    created_at=Column(DateTime(timezone=True),server_default=func.now())

    __table_args__=(
        Index("ix_device_time","device_id","timestamp",unique=True),
    )

