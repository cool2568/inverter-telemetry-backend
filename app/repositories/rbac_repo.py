from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.permission import Permission
from app.models.roles_permission import RolePermission
from app.models.user_role import UserRole

class RBACRepository:

    @staticmethod
    async def get_user_permissions(db:AsyncSession,user_id:int)->set[str]:
        stmt=(
            select(Permission.code)
            .join(RolePermission,RolePermission.permission_id==Permission.id)
            .join(UserRole,UserRole.role_id==RolePermission.role_id)
            .where(UserRole.user_id==user_id)
        )
        result=await db.execute(stmt)
        return {row[0] for row in result.all()}
