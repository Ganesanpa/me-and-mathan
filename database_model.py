from sqlalchemy import Integer, String, Float, Column
from sqlalchemy.orm import Mapped
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Products(Base):
    __tablename__ = "Products"
    
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)  # type: ignore
    name: Mapped[str] = Column(String)
    description: Mapped[str] = Column(String)
    price: Mapped[float] = Column(Float)  # Changed to Float for price
    quantity: Mapped[int] = Column(Integer)  # Changed to Integer for quantity
