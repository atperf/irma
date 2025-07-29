from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime
import enum

class ActionStatus(str, enum.Enum):
    pending = 'pending'
    done = 'done'

class Action(Base):
    __tablename__ = 'actions'

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey('tickets.id'))
    description = Column(Text, nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'))
    status = Column(Enum(ActionStatus), default=ActionStatus.pending)
    due_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

    ticket = relationship('Ticket', back_populates='actions')
    owner = relationship('User')
