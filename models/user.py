from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class User(BaseModel, Base):
    _tablename_ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
