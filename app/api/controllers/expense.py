from fastapi import HTTPException

_expenses: list[dict] = []


def list_expenses() -> list[dict]:
    return _expenses


def get_expense(expense_id: int) -> dict:
    for expense in _expenses:
        if expense["id"] == expense_id:
            return expense
    raise HTTPException(status_code=404, detail="Expense not found")


def create_expense(payload: dict) -> dict:
    next_id = len(_expenses) + 1
    expense = {"id": next_id, **payload}
    _expenses.append(expense)
    return expense
