from pydantic import BaseModel
from typing import Optional

class TicketTemplateBase(BaseModel):
    name: str
    description: Optional[str] = None
    content: Optional[str] = None

class TicketTemplateCreate(TicketTemplateBase):
    pass

class TicketTemplate(TicketTemplateBase):
    id: int

    class Config:
        orm_mode = True
