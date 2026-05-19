from fastapi import APIRouter

router = APIRouter()

@router.get("/list")
def list_users():
    return {
        "users": [
            {
                "id": 1,
                "name": "User 1",
            }
        ]
    }

