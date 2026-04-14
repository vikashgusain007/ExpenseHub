from fastapi import APIRouter

router = APIRouter()


@router.get("/list")
def list_settlements():
    return {
        "settlements": [
            {
                "id": 1,
                "name": "Settlement 1",
            }
        ]
    }
