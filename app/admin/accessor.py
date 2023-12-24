from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import User


async def give_admin_rules(user_id: int, session: AsyncSession):
    stmt = update(User).where(User.id == user_id).values(is_admin=1)
    await session.execute(stmt)
    await session.commit()