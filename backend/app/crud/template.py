from sqlalchemy.orm import Session
from typing import List

from ..models.template import TicketTemplate
from ..schemas.template import TicketTemplateCreate


def create_template(db: Session, template_in: TicketTemplateCreate) -> TicketTemplate:
    template = TicketTemplate(**template_in.dict())
    db.add(template)
    db.commit()
    db.refresh(template)
    return template


def get_template(db: Session, template_id: int) -> TicketTemplate:
    return db.query(TicketTemplate).filter(TicketTemplate.id == template_id).first()


def get_templates(db: Session, skip: int = 0, limit: int = 100) -> List[TicketTemplate]:
    return db.query(TicketTemplate).offset(skip).limit(limit).all()
