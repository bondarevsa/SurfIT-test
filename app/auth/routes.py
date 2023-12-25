from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.auth import create_jwt_token
from app.auth.database_accessor import create_user, get_user_by_username
from app.auth.schemas import UserBase, UserCreate
from app.database.database import get_async_session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/register")
async def register_user(
    user: UserCreate, session: AsyncSession = Depends(get_async_session)
):
    hashed_password = pwd_context.hash(user.password)
    try:
        user = await create_user(user.email, user.username, hashed_password, session)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="This user already exist"
        )
    return user


@auth_router.post("/auth")
async def authenticate_user(
    user_request: UserBase, session: AsyncSession = Depends(get_async_session)
):
    user = await get_user_by_username(user_request.username, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    is_password_correct = pwd_context.verify(
        user_request.password, user.hashed_password
    )

    if not is_password_correct:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    jwt_token = await create_jwt_token({"sub": user.username})
    response = JSONResponse(content={"access_token": jwt_token, "token_type": "bearer"})
    response.set_cookie(key="access_token", value=jwt_token, max_age=3600)
    return response
