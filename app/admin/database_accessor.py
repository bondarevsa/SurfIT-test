from typing import List

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import Advertisement, Complaint, Review, User


async def give_admin_rules(user_id: int, session: AsyncSession) -> None:
    stmt = update(User).where(User.id == user_id).values(is_admin=True)
    await session.execute(stmt)
    await session.commit()


async def ban_user_by_id(user_id: int, session: AsyncSession) -> None:
    stmt = update(User).where(User.id == user_id).values(is_banned=True)
    await session.execute(stmt)
    await session.commit()


async def unban_user_by_id(user_id: int, session: AsyncSession) -> None:
    stmt = update(User).where(User.id == user_id).values(is_banned=False)
    await session.execute(stmt)
    await session.commit()


async def delete_review(review_id: int, session: AsyncSession) -> None:
    query = delete(Review).where(Review.id == review_id)
    await session.execute(query)
    await session.commit()


async def get_all_complaints(session: AsyncSession) -> List[Complaint]:
    query = select(Complaint)
    res = await session.execute(query)
    complaints = res.scalars().all()
    return complaints


async def change_advertisement_type(
    advertisement_id: int, advertisement_type: str, session
) -> None:
    stmt = (
        update(Advertisement)
        .where(Advertisement.id == advertisement_id)
        .values(adv_type=advertisement_type)
    )
    await session.execute(stmt)
    await session.commit()
