from sqlalchemy.orm import Session
from ..models.user import User, UserRole
from ..schemas.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_user(db: Session, user_in: UserCreate) -> User:
    hashed_password = get_password_hash(user_in.password)
    user = User(username=user_in.username, hashed_password=hashed_password, role=user_in.role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_username(db: Session, username: str) -> User:
    return db.query(User).filter(User.username == username).first()
