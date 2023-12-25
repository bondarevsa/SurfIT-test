from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import User


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
