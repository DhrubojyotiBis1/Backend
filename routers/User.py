from fastapi import APIRouter, Depends
from Backend.Config.query import get_db, Query
from Backend.Schemas.User import User 

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
    )

query = Query()

@router.post("/signup")
async def create_user(user: User, db = Depends(get_db)):
    #check if email and phonr number is valid 
    await query.insertUser(db, user.name, user.mail, user.phone, user.type)
    return {"description": "Working"}