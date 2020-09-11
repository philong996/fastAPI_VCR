from app.api import crud
from app.api.models import TransactionSchema, TransactionDB
from fastapi import APIRouter, HTTPException


router = APIRouter()

@router.post("/", response_model=TransactionDB, status_code=201)
async def add_customer(payload: TransactionSchema):
    transaction_id = await crud.insert_transaction(payload)

    response_object = {
        "id" : transaction_id,
        "trans_code" : payload.trans_code,
        "customer_id" : payload.customer_id,
        "product_id" : payload.product_id,
        "promotion_code" : payload.promotion_code,
        "diamond_code": payload.diamond_code,
        "discount_diamond": payload.discount_diamond,
        "price_diamond" : payload.price_diamond,
        "price" : payload.price,
        "discount" : payload.discount,
        "source" : payload.source,
        "store" : payload.store,
        "discount" : payload.discount,
        "created_date": payload.created_date
    }
    return response_object


@router.get("/{id}", response_model=TransactionDB)
async def get_product_id(id: int):
    trans = await crud.get_by_id("transaction", id)

    return trans