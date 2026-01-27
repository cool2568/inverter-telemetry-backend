from sqlalchemy import Column,Interger,String
from app.models.base import Base,AuditMixin

class Role(Base,AuditMixin):
    __tablename__="roles"

    id=Column(Interger,primary_key=True)
    name=Column(String(50),unique=True,nullable=False)
    description=Column(String(255),nullable=True)

    