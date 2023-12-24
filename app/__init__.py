from fastapi import FastAPI


app = FastAPI(title="SurfIT test")

from app.auth.routes import auth_router
from app.main.routes import main_router
from app.admin.routes import admin_router

app.include_router(auth_router)
app.include_router(main_router)
app.include_router(admin_router)
