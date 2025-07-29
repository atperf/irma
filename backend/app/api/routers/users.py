from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ...schemas.user import User, UserCreate
from ...crud import user as crud_user
from ...models.user import User as UserModel
from ..deps import get_db, require_role
from ...models.user import UserRole

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=User)
def create_user(user_in: UserCreate, db: Session = Depends(get_db), user=Depends(require_role(UserRole.admin))):
    return crud_user.create_user(db, user_in)


@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Admin only for this example
    require_role(UserRole.admin)
    return db.query(UserModel).offset(skip).limit(limit).all()
