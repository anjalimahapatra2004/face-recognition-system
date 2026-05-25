from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.auth_routes import router

from app.database.connection import engine
from app.database.base import Base

# Import model so SQLAlchemy can detect table
from app.models.user_model import User

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")