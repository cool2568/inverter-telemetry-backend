from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.users import get_current_user
from app.services.rbac_service import RBACService
from app.core.database import get_db

def require_permission(permission_code: str):
    async def dependency(
        current_user=Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
    ):
        await RBACService.require_permission(
            db,
            current_user.id,
            permission_code
        )
        return current_user

    return dependency