from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DateTime, Boolean, Integer
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass


class AuditMixin:
    """
    Base audit fields for all tables
    """
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
    is_active = Column(
        Boolean,
        default=True,
        nullable=False
    )
    created_by = Column(
        Integer,
        nullable=True,
        index=True
    )
    updated_by = Column(
        Integer,
        nullable=True,
        index=True
    )
