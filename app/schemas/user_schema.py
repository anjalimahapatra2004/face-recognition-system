from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr

class UserResponse(BaseModel):
    uuid: str
    full_name: str
    email: EmailStr

    class Config:
        from_attributes = True