from pydantic import BaseModel

class RegisterPayload(BaseModel):
    name: str
    email: str
    password: str

class RegisterResponse(BaseModel):
    message: str

class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str

class LoginPayload(BaseModel):
    email: str
    password: str
