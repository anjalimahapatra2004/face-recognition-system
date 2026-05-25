from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.exc import IntegrityError
from app.services.face_service import FaceService
from app.database.connection import SessionLocal
from app.models.user_model import User
import face_recognition
import numpy as np

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


# ================= REGISTER PAGE =================

@router.get("/register")
async def register_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="register.html"
    )


# ================= LOGIN PAGE =================

@router.get("/login")
async def login_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )


# ================= REGISTER FACE =================

@router.post("/register-face")
async def register_face(request: Request):

    data = await request.json()

    name = data.get("name")
    email = data.get("email")
    image = data.get("image")

    if not image:
        return JSONResponse(
            status_code=400,
            content={
                "message": "No Image Received"
            }
        )

    try:

        image_data = image.split(",")[1]

        encoding = FaceService.generate_face_encoding(
            image_data
        )

        if encoding is None:
            return JSONResponse(
                status_code=400,
                content={
                    "message": "No Face Detected"
                }
            )

        db = SessionLocal()

        new_user = User(
            name=name,
            email=email,
            face_encoding=str(encoding)
        )

        try:

            db.add(new_user)
            db.commit()
            db.refresh(new_user)

        except IntegrityError:

            db.rollback()

            return JSONResponse(
                status_code=400,
                content={
                    "message": "Email already registered"
                }
            )

        return {
            "message": "Face Registered Successfully"
        }

    except Exception as e:

        print("ERROR:", e)

        return JSONResponse(
            status_code=500,
            content={
                "message": str(e)
            }
        )


# ================= LOGIN FACE =================

@router.post("/login-face")
async def login_face(request: Request):

    data = await request.json()

    image = data.get("image")

    if not image:
        return JSONResponse(
            status_code=400,
            content={
                "message": "No Image Received"
            }
        )

    try:

        image_data = image.split(",")[1]

        login_encoding = FaceService.generate_face_encoding(
            image_data
        )

        if login_encoding is None:
            return JSONResponse(
                status_code=400,
                content={
                    "message": "No Face Detected"
                }
            )

        login_encoding = np.array(
            login_encoding,
            dtype=np.float64
        )

        db = SessionLocal()

        users = db.query(User).all()

        for user in users:

            stored_encoding = np.array(
                eval(user.face_encoding),
                dtype=np.float64
            )

            match = face_recognition.compare_faces(
                [stored_encoding],
                login_encoding
            )[0]

            if match:

                return {
                    "message": f"Welcome {user.name}"
                }

        return JSONResponse(
            status_code=401,
            content={
                "message": "Face Not Matched"
            }
        )

    except Exception as e:

        print("ERROR:", e)

        return JSONResponse(
            status_code=500,
            content={
                "message": str(e)
            }
        )