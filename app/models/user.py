from sqlalchemy import Column,Integer,String,Boolean
from app.models.base import Base,AuditMixin

class User(Base,AuditMixin):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    email=Column(String(255),unique=True,index=True,nullable=False)
    hashed_password=Column(String,nullable=False)
    