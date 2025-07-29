from sqlalchemy.orm import Session
from typing import List

from ..models.ticket import Ticket
from ..models.action import Action
from ..schemas.ticket import TicketCreate


def create_ticket(db: Session, ticket_in: TicketCreate, user_id: int) -> Ticket:
    ticket = Ticket(title=ticket_in.title, description=ticket_in.description, creator_id=user_id)
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def get_ticket(db: Session, ticket_id: int) -> Ticket:
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def get_tickets(db: Session, skip: int = 0, limit: int = 100) -> List[Ticket]:
    return db.query(Ticket).offset(skip).limit(limit).all()
