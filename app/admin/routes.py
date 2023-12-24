from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import app
from app.admin.accessor import give_admin_rules
from app.admin.admin import get_current_admin
from app.database import User
from app.database.database import get_async_session


@app.put('/admin-rules/{id}', response_model=dict)
async def update_is_admin(
        id: int,
        current_admin: User = Depends(get_current_admin),
        session: AsyncSession = Depends(get_async_session)
):
    await give_admin_rules(id, session)
    return {'message': 'ok'}
