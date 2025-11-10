from fastapi import APIRouter, HTTPException
from .models import List

router = APIRouter()

db = []

@router.get("/")
async def home():
    return {"message": "success"}

@router.post("/to_do_list")
async def create_to_do_list(to_do_list: List):
    if any(l.username == to_do_list.username for l in db):
        return HTTPException(status_code=400, detail="the list exists")

    to_do_list.status = True
    db.append(to_do_list)
    return {
        "responce": 200,
        "message": "success"
    }