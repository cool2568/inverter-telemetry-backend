from datetime import datetime,timedelta,timezone
from passlib.context import CryptContext
from jose import jwt
from app.core.config import settings

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str)->str:
    return pwd_context.hash(password)


def verify_password(password:str,hashed:str)->bool:
    return pwd_context.verify(password,hashed)

def create_acess_token(user_id:int)->str:
    payload={
        "sub":str(user_id),
        "exp":datetime.now(timezone.utc) + timedelta(days=settings.ACCESS_TOKEN_EXPIRE_DAYS)
    }
    return jwt.encode(
        payload,settings.JWT_SECRET,algorithm=settings.JWT_ALGORITHM
    )

