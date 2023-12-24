from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

from app import app
from app.auth.auth import create_jwt_token
from app.database.database import get_async_session
from app.auth.accessor import create_user, get_user_by_username

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@app.post("/register")
async def register_user(email: str, username: str, password: str, session: AsyncSession = Depends(get_async_session)):
    hashed_password = pwd_context.hash(password)
    user = await create_user(email, username, hashed_password, session)
    return {"username": user.username, "hashed_password": user.hashed_password}


@app.post("/auth")
async def authenticate_user(username: str, password: str, session: AsyncSession = Depends(get_async_session)):
    user = await get_user_by_username(username, session)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    is_password_correct = pwd_context.verify(password, user.hashed_password)

    if not is_password_correct:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    jwt_token = await create_jwt_token({"sub": user.username})
    response = JSONResponse(content={"access_token": jwt_token, "token_type": "bearer"})
    response.set_cookie(key="access_token", value=jwt_token, max_age=3600)
    return response
