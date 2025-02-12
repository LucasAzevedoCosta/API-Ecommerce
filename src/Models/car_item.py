from sqlalchemy import Column, Integer, ForeignKey, Float
from Database.database import Base



class CarItem(Base):
    __tablename__ = "car_items"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)