from fastapi import APIRouter

router = APIRouter()


@router.get("/list")
def list_groups():
    return {
        "groups": [
            {
                "id": 1,
                "name": "Group 1",
            }
        ]
    }
