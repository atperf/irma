from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ...schemas.template import TicketTemplate, TicketTemplateCreate
from ...crud import template as crud_template
from ..deps import get_db, require_role
from ...models.user import UserRole

router = APIRouter(prefix="/templates", tags=["templates"])


@router.post("/", response_model=TicketTemplate)
def create_template(template_in: TicketTemplateCreate, db: Session = Depends(get_db), user=Depends(require_role(UserRole.supervisor))):
    return crud_template.create_template(db, template_in)


@router.get("/", response_model=List[TicketTemplate])
def read_templates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_template.get_templates(db, skip=skip, limit=limit)
