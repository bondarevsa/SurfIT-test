from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import app
from app.auth.auth import get_current_user
from app.database import User
from app.database.database import get_async_session
from app.main.accessor import create_advertisement


@app.post('/advertisements')
async def get_advertisements(
        body: str,
        adv_type: str,
        header: str,
        current_user: User = Depends(get_current_user),
        session: AsyncSession = Depends(get_async_session)
):
    advertisements = await create_advertisement(body, adv_type, header, current_user.id, session)
    return advertisements
