from pydantic import BaseModel

class InverterCreate(BaseModel):
    device_uid:str
    name:str
    model_number:str|None=None
    manufacturer:str|None=None


class InverterOut(BaseModel):
    id: int
    name: str
    serial_number: str
    model_number: str | None
    manufacturer: str | None

    class Config:
        from_attributes = True