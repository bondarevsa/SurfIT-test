from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.advertisements.database_accessor import (
    create_advertisement,
    create_review,
    delete_advertisement_by_id,
    get_advertisement_by_id,
    get_all_advertisements,
)
from app.advertisements.schemas import (
    AdvertisementBase,
    AdvertisementCreate,
    ReviewCreate,
)
from app.auth.auth import get_current_user
from app.database import Advertisement, SortColumnType, SortDirectionType, User
from app.database.database import get_async_session

advertisement_router = APIRouter(tags=["advertisements"])


@advertisement_router.get("/advertisements", response_model=List[AdvertisementBase])
async def get_advertisements(
    limit: Optional[int] = Query(None),
    offset: Optional[int] = Query(None),
    sort_column: Optional[SortColumnType] = Query(None),
    sort_direction: Optional[SortDirectionType] = Query(None),
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
):
    if not sort_column:
        sort_column = "created_at"
    advertisements = await get_all_advertisements(
        session, limit, offset, sort_column, sort_direction
    )
    return advertisements


@advertisement_router.post("/advertisements", response_model=Advertisement)
async def create_advertisements(
    advertisement: AdvertisementCreate,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
):
    advertisement = await create_advertisement(
        advertisement.body,
        advertisement.adv_type,
        advertisement.header,
        current_user.id,
        session,
    )
    return advertisement


@advertisement_router.delete("/advertisements/{id}", response_model=dict)
async def delete_advertisements(
    id: int = Path(),
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
):
    advertisement = await get_advertisement_by_id(id, session)
    if not advertisement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Advertisement not found"
        )

    if current_user.id == advertisement.created_by:
        await delete_advertisement_by_id(id, session)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="It is not your advertisement"
        )
    return {"message": "ok"}


@advertisement_router.get("/advertisements/{id}", response_model=Advertisement)
async def get_advertisement(
    id: int,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
):
    advertisement = await get_advertisement_by_id(id, session)
    if not advertisement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Advertisement not found"
        )
    return advertisement


@advertisement_router.post("/advertisements/{id}/reviews")
async def create_reviews(
    review: ReviewCreate,
    id: int = Path(),
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
):
    try:
        review = await create_review(
            review.text, current_user.id, review.rating, id, session
        )
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Advertisement not found."
        )
    return review
