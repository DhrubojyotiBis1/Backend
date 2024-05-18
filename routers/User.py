from fastapi import APIRouter
from Backend.Config.database import Base, engine

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
    )

@router.post("/signup")
async def read_users():
    Base.metadata.create_all(engine, tables=["user"])
    #ADD user logic
    return {"description": "Working"}