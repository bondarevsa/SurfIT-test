from sqlalchemy import select, desc, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import Advertisement, User


async def create_advertisement(body: str, adv_type: str, header: str, user_id: int, session: AsyncSession):
    advertisement = Advertisement(body=body, adv_type=adv_type, header=header, user_id=user_id)
    session.add(advertisement)
    await session.commit()
    return advertisement


async def get_all_advertisements(session: AsyncSession):
    query = select(Advertisement).order_by(desc(Advertisement.timestamp))
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
