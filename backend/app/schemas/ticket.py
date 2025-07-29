from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum

class TicketStatus(str, Enum):
    open = 'open'
    in_progress = 'in_progress'
    closed = 'closed'

class ActionStatus(str, Enum):
    pending = 'pending'
    done = 'done'

class Action(BaseModel):
    id: int
    description: str
    owner_id: int
    status: ActionStatus
    due_date: Optional[datetime] = None

    class Config:
        orm_mode = True

class TicketBase(BaseModel):
    title: str
    description: Optional[str] = None

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: int
    status: TicketStatus
    created_at: datetime
    updated_at: datetime
    creator_id: int
    actions: List[Action] = []

    class Config:
        orm_mode = True
