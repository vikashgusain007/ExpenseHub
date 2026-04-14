from fastapi import APIRouter
from fastapi import Body

from app.api.controllers import user as user_controller

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def list_users():
    return user_controller.list_users()


@router.get("/{user_id}")
def get_user(user_id: int):
    return user_controller.get_user(user_id)


@router.post("/")
def create_user(payload: dict = Body(...)):
    return user_controller.create_user(payload)
