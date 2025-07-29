from fastapi import FastAPI

from .database import engine
from .models import base, user, ticket, action, template

base.Base.metadata.create_all(bind=engine)

from .api.routers import tickets, templates, users

app = FastAPI(title="IRMA")

app.include_router(users.router)
app.include_router(templates.router)
app.include_router(tickets.router)
