from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.accessor import get_user_by_username
from app.auth.auth import get_current_user
from app.database import User
from app.database.database import get_async_session


async def get_current_admin(
        current_user: User = Depends(get_current_user),
        session: AsyncSession = Depends(get_async_session)
):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail='You are not admin')
    admin = await get_user_by_username(current_user.username, session)
    return admin
