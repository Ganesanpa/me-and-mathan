
from pydantic import BaseModel
class Products(BaseModel):
    id:int
    name:str
    description:str
    price:float
    quantity:int



    def __int__(self,id:int,name:str,description:str,price:float,quantity:int):
        self.id=id
        self.name=name
        self.description=description
        self.price=price
        self.quantity=quantity


