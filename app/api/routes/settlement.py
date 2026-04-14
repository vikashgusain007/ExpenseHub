from fastapi import APIRouter

from app.api.controllers import settlement as settlement_controller

router = APIRouter(prefix="/settlements", tags=["settlements"])


@router.get("/")
def list_settlements():
    return settlement_controller.list_settlements()


@router.post("/group/{group_id}")
def settle_group(group_id: int):
    return settlement_controller.settle_group(group_id)
