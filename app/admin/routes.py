from fastapi import Depends, APIRouter, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.admin.accessor import give_admin_rules, ban_user_by_id, unban_user_by_id
from app.admin.admin import get_current_admin
from app.database import User
from app.database.database import get_async_session

admin_router = APIRouter(prefix="/admin", tags=["admin"])


@admin_router.put('/give-rules/{id}', response_model=dict)
async def update_is_admin(
        id: int = Path(),
        current_admin: User = Depends(get_current_admin),
        session: AsyncSession = Depends(get_async_session)
):
    await give_admin_rules(id, session)
    return {'message': 'ok'}


@admin_router.put('/ban-users/{id}', response_model=dict)
async def ban_users(
        id: int = Path(),
        current_admin: User = Depends(get_current_admin),
        session: AsyncSession = Depends(get_async_session)
):
    await ban_user_by_id(id, session)
    return {'message': 'ok'}


@admin_router.put('/unban-users/{id}', response_model=dict)
async def unban_users(
        id: int = Path(),
        current_admin: User = Depends(get_current_admin),
        session: AsyncSession = Depends(get_async_session)
):
    await unban_user_by_id(id, session)
    return {'message': 'ok'}
