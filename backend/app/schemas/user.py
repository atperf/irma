from pydantic import BaseModel
from enum import Enum

class UserRole(str, Enum):
    admin = 'admin'
    supervisor = 'supervisor'
    operator = 'operator'
    guest = 'guest'

class UserBase(BaseModel):
    username: str
    role: UserRole

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
