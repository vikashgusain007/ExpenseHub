from fastapi import APIRouter

router = APIRouter()


@router.get("/list")
def list_expenses():
    return {
        "expenses": [
            {
                "id": 1,
                "name": "Expense 1",
                "amount": 100,
            }
        ]
    }
