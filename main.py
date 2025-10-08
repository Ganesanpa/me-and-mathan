from fastapi import Depends,FastAPI, HTTPException

from pydantic import BaseModel
import database_model
from model import Products


from database import session,engine

database_model.Base.metadata.create_all(bind=engine) # type: ignore

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
def int_db():
    db=session() # type: ignore
    count=db.query(database_model.Products).count
    if count ==0:
      db.add(database_model.Product(**products.model_dump))
    db.commit()
int_db()


def get_db():
    db = SessionLocal() # type: ignore
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def getall(db:session=Depends(get_db)):
   db_products=db.query(database_model.Product).all()
   return db_products


@app.get("/products/{id}")
def hello(id:int,db:session=Depends(get_db)):
    one_product=db.query(database_model.Products).filter(Products.id==id).first()
    if one_product is None:
        raise HTTPException(status_code=404,detail='Products not found')
    return one_product
  


@app.post("/product")
def add_product(product:Products,db:session=Depends(get_db)):
    add_new_product=database_model.Products(**product.model_dump)
    db.add(add_new_product)
    db.commit()
    return add_new_product


@app.put("/product")
def update_product(id:int,product:Products,db:session=Depends(get_db)):
    update_product=db.query(database_model.Products).filter(Products.id==id).first()
    if not update_product:
         raise HTTPException(status_code=404,detail='Products not found')
    update_product.name=product.name
    update_product.description=product.description
    update_product.price=product.price
    update_product.quantity=product.quantity
    db.commit()
    db.refresh(update_product)
    return "pruduct updated successfully"  
    



@app.delete("/products")
def delete_product(id:int,db:session=Depends(get_db)):
    update_product=db.query(database_model.Products).filter(Products.id==id).first()
    if not update_product:
         raise HTTPException(status_code=404,detail='Products not found')
    db.delete(update_product)
    db.commit()
    return {"message": "Item deleted successfully"}
  # main.py
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
import database_model
from model import Products
from database import session, engine

database_model.Base.metadata.create_all(bind=engine)  # type: ignore

app = FastAPI()

# Initialize database with default products
def int_db():
    db = session()  # type: ignore
    count = db.query(database_model.Products).count()
    if count == 0:
        for product in products:
            db.add(database_model.Products(**product.dict()))  # Correcting this line
        db.commit()

# Example products to add
products = [
    Products(id=1, name="game", description="nothing", price=150.6, quantity=2),
    Products(id=2, name="game", description="nothing", price=150.6, quantity=2),
    Products(id=3, name="game", description="nothing", price=150.6, quantity=2),
    Products(id=4, name="game", description="nothing", price=150.6, quantity=2),
    Products(id=5, name="game", description="nothing", price=150.6, quantity=2),
    Products(id=6, name="game", description="nothing", price=150.6, quantity=2),
    Products(id=7, name="game", description="nothing", price=150.6, quantity=2),
]

int_db()  # Initialize database on startup

def get_db():
    db = session()  # type: ignore
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def get_all_products(db: session = Depends(get_db)):  # Renamed session to db
    db_products = db.query(database_model.Products).all()
    return db_products

@app.get("/products/{id}")
def get_product(id: int, db: session = Depends(get_db)):  # Renamed session to db
    one_product = db.query(database_model.Products).filter(database_model.Products.id == id).first()
    if one_product is None:
        raise HTTPException(status_code=404, detail='Product not found')
    return one_product

@app.post("/product")
def add_product(product: Products, db: session = Depends(get_db)):  # Renamed session to db
    new_product = database_model.Products(**product.dict())  # Use .dict() to convert Pydantic model to SQLAlchemy
    db.add(new_product)
    db.commit()
    return new_product

@app.put("/product/{id}")
def update_product(id: int, product: Products, db: session = Depends(get_db)):  # Renamed session to db
    update_product = db.query(database_model.Products).filter(database_model.Products.id == id).first()
    if not update_product:
        raise HTTPException(status_code=404, detail='Product not found')
    
    update_product.name = product.name
    update_product.description = product.description
    update_product.price = product.price
    update_product.quantity = product.quantity
    db.commit()
    db.refresh(update_product)
    return "Product updated successfully"

@app.delete("/products/{id}")
def delete_product(id: int, db: session = Depends(get_db)):  # Renamed session to db
    product_to_delete = db.query(database_model.Products).filter(database_model.Products.id == id).first()
    if not product_to_delete:
        raise HTTPException(status_code=404, detail='Product not found')
    
    db.delete(product_to_delete)
    db.commit()
    return {"message": "Product deleted successfully"}
