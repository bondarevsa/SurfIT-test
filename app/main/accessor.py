from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import Advertisement


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
