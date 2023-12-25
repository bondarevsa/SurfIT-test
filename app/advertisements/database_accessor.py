from typing import List

from sqlalchemy import asc, delete, desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import Advertisement, Complaint, Review


async def create_advertisement(
    body: str, adv_type: str, header: str, created_by: int, session: AsyncSession
) -> Advertisement:
    advertisement = Advertisement(
        body=body, adv_type=adv_type, header=header, created_by=created_by
    )
    session.add(advertisement)
    await session.commit()
    return advertisement


async def get_all_advertisements(
    session: AsyncSession,
    limit: int = 10,
    offset: int = 0,
    sort_column: str = "created_at",
    sort_direction: str = "desc",
) -> List[Advertisement]:
    query = (
        select(Advertisement)
        .order_by(asc(sort_column) if sort_direction == "asc" else desc(sort_column))
        .limit(limit)
        .offset(offset)
    )
    res = await session.execute(query)
    advertisements = res.scalars().all()
    return advertisements


async def get_advertisement_by_id(
    advertisement_id: int, session: AsyncSession
) -> Advertisement:
    query = select(Advertisement).where(Advertisement.id == advertisement_id)
    res = await session.execute(query)
    return res.scalar_one_or_none()


async def delete_advertisement_by_id(ad_id, session: AsyncSession) -> None:
    query = delete(Advertisement).where(Advertisement.id == ad_id)
    await session.execute(query)
    await session.commit()


async def create_review(
    text: str,
    created_by: int,
    rating: int,
    advertisement_id: int,
    session: AsyncSession,
) -> Review:
    review = Review(
        text=text,
        created_by=created_by,
        rating=rating,
        advertisement_id=advertisement_id,
    )
    session.add(review)
    await session.commit()
    return review


async def create_complaint(
    text: str,
    complaint_type: str,
    created_by: int,
    advertisement_id: int,
    session: AsyncSession,
):
    complaint = Complaint(
        text=text,
        complaint_type=complaint_type,
        created_by=created_by,
        advertisement_id=advertisement_id,
    )
    session.add(complaint)
    await session.commit()
    return complaint
