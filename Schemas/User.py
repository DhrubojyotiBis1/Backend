from pydantic import BaseModel

class User(BaseModel):
    name: str 
    phone: str
    mail: str
    type: str = 0