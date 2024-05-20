from ..Config.db import Base
from sqlalchemy import Column, String, Integer

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50))
    mail = Column(String(length=100))
    phone = Column(String(length=15))
    type = Column(Integer, default=0)
    #add created date