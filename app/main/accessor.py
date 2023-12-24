from sqlalchemy import select, desc, delete, asc
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import Advertisement, User, Review


async def create_advertisement(body: str, adv_type: str, header: str, user_id: int, session: AsyncSession):
    advertisement = Advertisement(body=body, adv_type=adv_type, header=header, user_id=user_id)
    session.add(advertisement)
    await session.commit()
    return advertisement


async def get_all_advertisements(sort_column_obj, session: AsyncSession, limit: int = 10, offset: int = 0, sort_direction: str = 'desc'):
    query = (
        select(Advertisement)
        .order_by(asc(sort_column_obj) if sort_direction == "asc" else desc(sort_column_obj))
        .limit(limit)
        .offset(offset)
    )
    res = await session.execute(query)
    advertisements = res.scalars().all()
    return advertisements


async def get_advertisement_by_id(advertisement_id: int, session: AsyncSession):
    query = select(Advertisement).where(Advertisement.id == advertisement_id)
    res = await session.execute(query)
    return res.scalar_one_or_none()


async def delete_advertisement_by_id(ad_id, session: AsyncSession):
    query = delete(Advertisement).where(Advertisement.id == ad_id)
    await session.execute(query)
    await session.commit()


async def create_review(text: str, user_id: int, rating: int, advertisement_id: int, session: AsyncSession):
    review = Review(text=text, user_id=user_id, rating=rating, advertisement_id=advertisement_id)
    session.add(review)
    await session.commit()
    return review
