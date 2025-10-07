from fastapi import FastAPI

from pydantic import BaseModel
from model import Products


from database import session,engine

database_model.Base.metadata.create_all()

app=FastAPI()
products=[
    Products(id=1,name="game",description="nothing",price=150.6,quantity=2),
    Products(id=2,name="game",description="nothing",price=150.6,quantity=2),
    Products(id=3,name="game",description="nothing",price=150.6,quantity=2),
    Products(id=4,name="game",description="nothing",price=150.6,quantity=2),
    Products(id=5,name="game",description="nothing",price=150.6,quantity=2),
    Products(id=6,name="game",description="nothing",price=150.6,quantity=2),
    Products(id=7,name="game",description="nothing",price=150.6,quantity=2),
]


@app.get("/")
def getall():
   return products


@app.get("/products/{id}")
def hello(id:int):
    for product in products:
        if product.id==id:
            return product
    return "Product not found"


@app.post("/product")
def add_product(product:Products):
    products.append(product)
    return product


@app.put("/product")
def update_product(id:int,product:Products):
    for i in range(len(products)):
        if products[i].id==id:
            products[i]=product
        return "pruduct updated successfully"  
    return "No product found"



@app.delete("/products")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
        return "Product deleted successfully"
    return "Product not found"    