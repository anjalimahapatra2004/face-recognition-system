from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.controllers.auth_controller import router as auth_router

router = APIRouter()

@router.get("/register", response_class=HTMLResponse)
async def register_page():

    with open("app/templates/register.html", "r") as file:
        return file.read()

router.include_router(auth_router)