from sqlalchemy import Column, Integer, String, Enum
from .base import Base
import enum

class UserRole(str, enum.Enum):
    admin = 'admin'
    supervisor = 'supervisor'
    operator = 'operator'
    guest = 'guest'

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.operator)
