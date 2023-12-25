from fastapi import FastAPI

from app.admin.routes import admin_router
from app.advertisements.routes import advertisement_router
from app.auth.routes import auth_router


def get_application() -> FastAPI:
    application = FastAPI(title="SurfIT test")
    application.include_router(auth_router)
    application.include_router(advertisement_router)
    application.include_router(admin_router)
    return application


app = get_application()
