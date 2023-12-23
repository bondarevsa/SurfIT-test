from sqlalchemy.ext.asyncio import AsyncSession

from app.database import Advertisement


async def create_advertisement(body: str, adv_type: str, header: str, user_id: int, session: AsyncSession):
    advertisement = Advertisement(body=body, adv_type=adv_type, header=header, user_id=user_id)
    session.add(advertisement)
    await session.commit()
    return advertisement
