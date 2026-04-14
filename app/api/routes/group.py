from fastapi import APIRouter
from fastapi import Body

from app.api.controllers import group as group_controller

router = APIRouter(prefix="/groups", tags=["groups"])


@router.get("/")
def list_groups():
    return group_controller.list_groups()


@router.get("/{group_id}")
def get_group(group_id: int):
    return group_controller.get_group(group_id)


@router.post("/")
def create_group(payload: dict = Body(...)):
    return group_controller.create_group(payload)
