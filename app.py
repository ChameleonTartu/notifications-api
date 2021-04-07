from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Notification(BaseModel):
    created: bool


app = FastAPI()


@app.get("/")
async def ping():
    return {"message": "Pong"}


@app.post("/notification/")
async def create_notification(notification: Notification):
    print(notification)
    return notification
