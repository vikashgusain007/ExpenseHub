from fastapi import HTTPException

_groups: list[dict] = []


def list_groups() -> list[dict]:
    return _groups


def get_group(group_id: int) -> dict:
    for group in _groups:
        if group["id"] == group_id:
            return group
    raise HTTPException(status_code=404, detail="Group not found")


def create_group(payload: dict) -> dict:
    next_id = len(_groups) + 1
    group = {"id": next_id, **payload}
    _groups.append(group)
    return group
