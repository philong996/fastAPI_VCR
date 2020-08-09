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
        "price" : payload.price,
        "discount" : payload.discount,
        "source" : payload.source,
        "store" : payload.store,
        "discount" : payload.discount,
        "created_date": payload.created_date
    }
    return response_object