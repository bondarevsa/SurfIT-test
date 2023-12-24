from typing import List, Optional

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.auth import get_current_user
from app.database import User
from app.database.database import get_async_session
from app.main.accessor import create_advertisement, get_all_advertisements, delete_advertisement_by_id, \
    get_advertisement_by_id
from app.main.schemas import AllAdvertisements, AdvertisementBase

main_router = APIRouter(tags=["main"])


@main_router.get('/advertisements', response_model=List[AllAdvertisements])
async def get_advertisements(
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        current_user: User = Depends(get_current_user),
        session: AsyncSession = Depends(get_async_session)
):
    advertisements = await get_all_advertisements(session, limit, offset)
    return advertisements


@main_router.post('/advertisements', response_model=AdvertisementBase)
async def create_advertisements(
        body: str,
        adv_type: str,
        header: str,
        current_user: User = Depends(get_current_user),
        session: AsyncSession = Depends(get_async_session)
):
    advertisement = await create_advertisement(body, adv_type, header, current_user.id, session)
    return advertisement


@main_router.delete('/advertisements', response_model=dict)
async def delete_advertisements(
        advertisement_id: int,
        current_user: User = Depends(get_current_user),
        session: AsyncSession = Depends(get_async_session)
):
    advertisement = await get_advertisement_by_id(advertisement_id, session)
    if not advertisement:
        raise HTTPException(status_code=400, detail="Advertisement not found")

    if current_user.id == advertisement.user_id:
        await delete_advertisement_by_id(advertisement_id, session)
    else:
        raise HTTPException(status_code=400, detail="It is not your advertisement")
    return {"message": "ok"}


@main_router.get('/advertisements/{id}', response_model=AdvertisementBase)
async def get_advertisement(
        id: int,
        current_user: User = Depends(get_current_user),
        session: AsyncSession = Depends(get_async_session)
):
    advertisement = await get_advertisement_by_id(id, session)
    return advertisement

