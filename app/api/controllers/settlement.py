def list_settlements() -> list[dict]:
    return []


def settle_group(group_id: int) -> dict:
    # Placeholder response until balance service is implemented.
    return {
        "group_id": group_id,
        "status": "settled",
        "transactions": [],
    }
