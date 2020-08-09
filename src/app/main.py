from fastapi import FastAPI 
from app.api import ping, customer, product
from app.db import engine, metadata, database

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(ping.router)
app.include_router(customer.router, prefix="/customer", tags=["customer"])
app.include_router(product.router, prefix="/product", tags=["product"])