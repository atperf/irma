from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from .base import Base
from .user import User
import enum
from datetime import datetime

class TicketStatus(str, enum.Enum):
    open = 'open'
    in_progress = 'in_progress'
    closed = 'closed'

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    status = Column(Enum(TicketStatus), default=TicketStatus.open)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    creator_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship('User', backref='tickets')
    actions = relationship('Action', back_populates='ticket', cascade='all, delete-orphan')
