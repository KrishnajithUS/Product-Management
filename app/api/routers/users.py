from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from app.api.deps import SessionDep, get_current_active_superuser
from app.models.models import User, UserCreate, UserOut
from app.service import users


router = APIRouter()


@router.post(
    "/users",
    tags=["Users"],
    dependencies=[Depends(get_current_active_superuser)],
    response_model=UserOut,
)
def create_user(session: SessionDep, user_in: UserCreate) -> Any:
    """
    Create new user.
    """
    user = users.get_user_by_email(session=session, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )

    user = users.create_user(session=session, user_create=user_in)

    return user
