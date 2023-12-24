from fastapi import FastAPI

app = FastAPI(title="SurfIT test")

from app.auth import routes
from app.main import routes
from app.admin import routes
