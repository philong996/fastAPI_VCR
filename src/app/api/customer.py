from app.api import crud
from app.api.models import CustomerSchema, CustomerDB
from fastapi import APIRouter, HTTPException


router = APIRouter()

@router.post("/", response_model=CustomerDB, status_code=201)
async def add_customer(payload: CustomerSchema):
    customer_id = await crud.insert_customer(payload)

    response_object = {
        "id" : customer_id,
        "customer_code" : payload.customer_code,
        "gender" : payload.gender,
        "birthday" : payload.birthday,
        "district" : payload.district,
        "city" : payload.city,
        "email" : payload.email,
        "first_purchase_date" : payload.first_purchase_date
    }
    return response_object


@router.get("/", response_model=CustomerDB)
async def get_product(customer_code: str):
    customer = await crud.get_at("customers", customer_code)

    return customer

@router.get("/{id}", response_model=CustomerDB)
async def get_product_id(id: int):
    customer = await crud.get_by_id("customers", id)

    return customer