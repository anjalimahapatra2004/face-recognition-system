from pydantic import BaseModel


class FaceLoginSchema(BaseModel):

    image: str


class FaceRegisterSchema(BaseModel):

    full_name: str

    email: str

    image: str