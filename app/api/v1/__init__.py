from fastapi import APIRouter
from app.api.v1.routes.user import router as user_router
from app.api.v1.routes.group import router as group_router
from app.api.v1.routes.expense import router as expense_router
from app.api.v1.routes.settlement import router as settlement_router
from app.api.v1.routes.auth import router as auth_router

api_router = APIRouter(prefix="/api/v1")


api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(user_router, prefix="/users", tags=["users"])
api_router.include_router(group_router, prefix="/groups", tags=["groups"])
api_router.include_router(expense_router, prefix="/expenses", tags=["expenses"])
api_router.include_router(settlement_router, prefix="/settlements", tags=["settlements"])
