from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ...schemas.ticket import Ticket, TicketCreate
from ...crud import ticket as crud_ticket
from ..deps import get_db, require_role
from ...models.user import UserRole

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.post("/", response_model=Ticket)
def create_ticket(ticket_in: TicketCreate, db: Session = Depends(get_db), user=Depends(require_role(UserRole.operator))):
    return crud_ticket.create_ticket(db, ticket_in, user.id)


@router.get("/", response_model=List[Ticket])
def read_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_ticket.get_tickets(db, skip=skip, limit=limit)


@router.get("/{ticket_id}", response_model=Ticket)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    return crud_ticket.get_ticket(db, ticket_id)
