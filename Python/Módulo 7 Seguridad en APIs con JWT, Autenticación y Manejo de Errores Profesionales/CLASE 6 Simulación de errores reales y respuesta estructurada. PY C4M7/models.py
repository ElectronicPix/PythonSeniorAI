from sqlalchemy import column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    id = column(Integer, primary_key=True, index=True)
    username = column(String, unique=True, index=True)
    password = column(String)
    role = column(String)