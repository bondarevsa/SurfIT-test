from typing import List

from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.admin.admin import get_current_admin
from app.admin.database_accessor import (
    ban_user_by_id,
    change_advertisement_type,
    delete_review,
    get_all_complaints,
    give_admin_rules,
    unban_user_by_id,
)
from app.admin.schemas import ComplaintBase
from app.database import AdvertisementType, User
from app.database.database import get_async_session

admin_router = APIRouter(prefix="/admins", tags=["admin"])


@admin_router.put("/users/{id}/give-rules", response_model=dict)
async def give_admin_rules_to_user(
    id: int = Path(),
    current_admin: User = Depends(get_current_admin),
    session: AsyncSession = Depends(get_async_session),
):
    await give_admin_rules(id, session)
    return {"message": "ok"}


@admin_router.put("/users/{id}/ban", response_model=dict)
async def ban_users(
    id: int = Path(),
    current_admin: User = Depends(get_current_admin),
    session: AsyncSession = Depends(get_async_session),
):
    await ban_user_by_id(id, session)
    return {"message": "ok"}


@admin_router.put("/users/{id}/unban", response_model=dict)
async def unban_users(
    id: int = Path(),
    current_admin: User = Depends(get_current_admin),
    session: AsyncSession = Depends(get_async_session),
):
    await unban_user_by_id(id, session)
    return {"message": "ok"}


@admin_router.delete("/reviews/{id}", response_model=dict)
async def delete_reviews(
    id: int = Path(),
    current_admin: User = Depends(get_current_admin),
    session: AsyncSession = Depends(get_async_session),
):
    await delete_review(id, session)
    return {"message": "ok"}


@admin_router.get("/complaints", response_model=List[ComplaintBase])
async def get_complaints(
    current_admin: User = Depends(get_current_admin),
    session: AsyncSession = Depends(get_async_session),
):
    complaints = await get_all_complaints(session)
    return complaints


@admin_router.put("/advertisements/{id}", response_model=dict)
async def change_advertisements_type(
    advertisement_type: AdvertisementType,
    id: int = Path(),
    current_admin: User = Depends(get_current_admin),
    session: AsyncSession = Depends(get_async_session),
):
    await change_advertisement_type(id, advertisement_type, session)
    return {"message": "ok"}
