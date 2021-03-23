from messenger import messenger 
from fastapi import APIRouter

routes= APIRouter()

routes.include_router(messenger.router,prefix="messenger/")
