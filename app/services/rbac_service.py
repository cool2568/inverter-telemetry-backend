from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.rbac_repo import RBACRepository

class RBACService:

    @staticmethod
    async def require_permission(
        db:AsyncSession,
        user_id:int,
        permission_code:str
    ):
        permissions = await RBACRepository.get_user_permissions(db, user_id)

        if permission_code not in permissions:
            raise HTTPException(
                status_code=403,
                detail=f"Permission '{permission_code}' required"
            )