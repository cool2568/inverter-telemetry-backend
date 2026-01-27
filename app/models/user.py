from sqlalchemy import Column,Interger,String,Boolean
from app.models.base import Base,AuditMixin

class User(Base,AuditMixin):
    __tablename__="users"
    id=Column(Interger,primary_key=True)
    email=Column(String(255),unique=True,Index=True,nullable=False)
    hashed_password=Column(String,nullable=False)
    