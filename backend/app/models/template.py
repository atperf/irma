from sqlalchemy import Column, Integer, String, Text
from .base import Base

class TicketTemplate(Base):
    __tablename__ = 'ticket_templates'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)
    content = Column(Text)  # JSON or structured data representing fields/questions
