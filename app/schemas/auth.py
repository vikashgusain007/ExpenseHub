from pydantic import BaseModel

class RegisterPayload(BaseModel):
    name: str
    email: str
    password: str

class RegisterResponse(BaseModel):
    message: str
