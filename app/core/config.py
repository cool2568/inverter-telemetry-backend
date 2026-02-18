from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL:str
    JWT_SECRET:str
    JWT_ALGORITHM:str="HS256"
    ACCESS_TOKEN_EXPIRE_DAYS: int =1

    class Config:
        env_file=".env"

settings=Settings()