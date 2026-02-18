from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.models.base import Base, AuditMixin

class Device(Base, AuditMixin):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True)

    # Hardware identity (from QR / firmware)
    device_uid = Column(String(100), unique=True, nullable=False, index=True)
    serial_number = Column(String(50), unique=True, nullable=False)

    # State
    is_registered = Column(Boolean, default=False)
    last_seen_at = Column(DateTime(timezone=True), nullable=True)