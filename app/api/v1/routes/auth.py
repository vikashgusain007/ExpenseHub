from sqlalchemy.orm import Session
from fastapi import APIRouter, Body, Depends, HTTPException, status

from app.api.v1.service.auth import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
)
from app.models.user import User
from app.schemas.auth import (
    RegisterPayload,
    RegisterResponse,
    LoginPayload,
    LoginResponse,
)
from database import get_db

router = APIRouter()


@router.post(
    "/register",
    response_model=RegisterResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    payload: RegisterPayload = Body(...),
    db: Session = Depends(get_db),
) -> RegisterResponse:
    try:
        if "@" not in payload.email or "." not in payload.email.split("@")[-1]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Enter a valid email address",
            )
        if len(payload.password) < 10:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password must be at least 10 characters",
            )

        if db.query(User).filter(User.email == payload.email).first():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )

        user = User(
            name=payload.name,
            email=payload.email,
            password_hash=hash_password(payload.password),
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        return RegisterResponse(message="User registered successfully")
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error occured as {e}",
        )

@router.post(
    "/login",
    response_model=LoginResponse,
    status_code=status.HTTP_200_OK,
)
async def login(
    payload: LoginPayload = Body(...),
    db: Session = Depends(get_db),
) -> LoginResponse:
    try:
        user = db.query(User).filter(User.email == payload.email).first()
        if not user and not verify_password(payload.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )
        access_token = create_access_token(data={"sub": user.email})
        refresh_token = create_refresh_token(data={"sub": user.email})
        return LoginResponse(
            access_token=access_token,
            refresh_token=refresh_token,
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error occured as {e}",
        )
