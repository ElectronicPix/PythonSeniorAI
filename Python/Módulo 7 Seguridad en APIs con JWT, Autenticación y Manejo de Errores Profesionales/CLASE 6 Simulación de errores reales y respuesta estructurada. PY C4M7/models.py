from sqlalchemy import column, Integer, String
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    id = column(Integer, primary_key=True, index=True)
    username = column(String, unique=True, index=True)
    password = column(String)
    role = column(String)
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)