from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..models.user import User, UserRole
from ..crud.user import get_user_by_username
from ..database import SessionLocal

# placeholder for actual auth

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(db: Session = Depends(get_db)) -> User:
    # In production, use OAuth2 or other mechanism; this is simple placeholder
    user = get_user_by_username(db, 'admin')
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not authenticated')
    return user


def require_role(role: UserRole):
    def dependency(user: User = Depends(get_current_user)):
        if user.role != role and user.role != UserRole.admin:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Insufficient privileges')
        return user
    return dependency
