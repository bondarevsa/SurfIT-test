import jwt
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.accessor import get_user_by_username
from app.database.database import get_async_session
from config import SECRET_KEY

ALGORITHM = "HS256"
EXPIRATION_TIME = timedelta(minutes=30)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def create_jwt_token(data: dict):
    expiration = datetime.utcnow() + EXPIRATION_TIME
    data.update({"exp": expiration})
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_jwt_token(token: str):
    try:
        decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_data
    except jwt.PyJWTError:
        return None


def get_current_user(token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(get_async_session)):
    decoded_data = verify_jwt_token(token)
    if not decoded_data:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = get_user_by_username(decoded_data["sub"], session)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    return user
