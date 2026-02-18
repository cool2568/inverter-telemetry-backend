from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import Base, AuditMixin

class Inverter(Base, AuditMixin):
    __tablename__ = "inverters"

    id = Column(Integer, primary_key=True)

    # Ownership
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    # Device mapping (hardware identity)
    device_id = Column(
        Integer,
        ForeignKey("devices.id"),
        nullable=False,
        unique=True,
        index=True
    )

    # Business identity
    name = Column(String(100), nullable=False)
    serial_number = Column(String(50), unique=True, nullable=False, index=True)
    model_number = Column(String(50), nullable=True)
    manufacturer = Column(String(100), nullable=True)
