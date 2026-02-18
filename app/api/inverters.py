from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.inverter import InverterCreate,InverterOut
from app.services.inverter_service import InverterService
from app.api.users import get_current_user
from app.api.deps import require_permission
from app.core.database import get_db

router=APIRouter(
    prefix="/inverters",
    tags=["Inverters"]
)

@router.post(
    "/",
    response_model=InverterOut
)
async def create_inverter(
    payload:InverterCreate,
    current_user=Depends(require_permission("create_inverter")),
    db: AsyncSession=Depends(get_db)
):
    return await InverterService.create_inverter(
        db=db,
        user_id=current_user.id,
        device_uid=payload.device_uid,
        name=payload.name,
        model_number=payload.model_number,
        manufacturer=payload.manufacturer
    )

@router.get(
    "/",
    response_model=list[InverterOut]
)
async def list_my_inverters(
    current_user=Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await InverterService.list_user_inverters(db, current_user.id)