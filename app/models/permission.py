from sqlalchemy import Integer,String,Column
from app.models.base import Base,AuditMixin

class Permission(Base,AuditMixin):
    __tablename__="permissions"

    id=Column(Integer,primary_key=True)
    code=Column(String(100),unique=True,nullable=False)
    description=Column(String(255),nullable=True)