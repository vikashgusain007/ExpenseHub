from fastapi import HTTPException

# In-memory placeholders until DB layer is wired.
_users: list[dict] = []


def list_users() -> list[dict]:
    return _users


def get_user(user_id: int) -> dict:
    for user in _users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


def create_user(payload: dict) -> dict:
    next_id = len(_users) + 1
    user = {"id": next_id, **payload}
    _users.append(user)
    return user
