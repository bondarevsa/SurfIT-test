from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import User


async def create_user(
    email: str, username: str, hashed_password: str, session: AsyncSession
) -> User:
    user = User(
        email=email, username=username, hashed_password=hashed_password, is_admin=0
    )
    session.add(user)
    await session.commit()
    return user


async def get_user_by_username(username: str, session: AsyncSession) -> User:
    query = select(User).where(User.username == username)
    res = await session.execute(query)
    return res.scalar_one_or_none()
