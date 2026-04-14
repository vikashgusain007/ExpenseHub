from fastapi import APIRouter
from fastapi import Body

from app.api.controllers import expense as expense_controller

router = APIRouter(prefix="/expenses", tags=["expenses"])


@router.get("/")
def list_expenses():
    return expense_controller.list_expenses()


@router.get("/{expense_id}")
def get_expense(expense_id: int):
    return expense_controller.get_expense(expense_id)


@router.post("/")
def create_expense(payload: dict = Body(...)):
    return expense_controller.create_expense(payload)
