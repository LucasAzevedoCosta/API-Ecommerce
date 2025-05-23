from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from Database.database import Base
from flask_login import UserMixin

class User(Base, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    cart =  relationship("CarItem", backref='user', lazy=True)
    role = Column(Enum('manager', 'customer', name='user_roles'), nullable=False)