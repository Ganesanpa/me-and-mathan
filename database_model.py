
from sqlalchemy import Integer,String,Float,Column
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
class Products(Base):
    __tablename__="Products"
    id:Column(Integer,primary_key=True,index=True)  # type: ignore
    name:Column(String) # type: ignore
    description:Column(String) # type: ignore
    price:Column(String) # type: ignore
    quantity:Column(String) # type: ignore