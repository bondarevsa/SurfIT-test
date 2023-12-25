from datetime import datetime, timedelta

import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.database_accessor import get_user_by_username
from app.database.database import get_async_session
from config import SECRET_KEY

ALGORITHM = "HS256"
EXPIRATION_TIME = timedelta(minutes=30)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/auth")


async def create_jwt_token(data: dict):
    expiration = datetime.utcnow() + EXPIRATION_TIME
    data.update({"exp": expiration})
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token


async def verify_jwt_token(token: str):
    try:
        decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_data
    except jwt.PyJWTError:
        return None


async def get_current_user(
    request: Request, session: AsyncSession = Depends(get_async_session)
):
    token = request.cookies.get("access_token")
    decoded_data = await verify_jwt_token(token)
    if not decoded_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    user = await get_user_by_username(decoded_data["sub"], session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    if user.is_banned:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User are banned"
        )
    return user
