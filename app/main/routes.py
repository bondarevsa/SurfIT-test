from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import app
from app.auth.auth import get_current_user
from app.database import User
from app.database.database import get_async_session
from app.main.accessor import create_advertisement, get_all_advertisements


@app.get('/advertisements')
async def get_advertisements(
        current_user: User = Depends(get_current_user),
        session: AsyncSession = Depends(get_async_session)
):
    advertisements = await get_all_advertisements(session)
    print(advertisements)
    return advertisements


@app.post('/advertisements')
async def create_advertisements(
        body: str,
        adv_type: str,
        header: str,
        current_user: User = Depends(get_current_user),
        session: AsyncSession = Depends(get_async_session)
):
    advertisement = await create_advertisement(body, adv_type, header, current_user.id, session)
    return advertisement
