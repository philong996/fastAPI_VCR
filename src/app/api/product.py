from app.api import crud
from app.api.models import ProductSchema, ProductDB
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/", response_model=ProductDB, status_code=201)
async def add_product(payload: ProductSchema):
    product_id = await crud.insert_product(payload)

    response_object = {
        "id" : product_id,
        "product_code": payload.product_code,
        "category": payload.category,
        "design_group": payload.design_group,
        "price_segment": payload.price_segment,
        "size_diamond" : payload.size_diamond
    }
    return response_object

@router.get("/{product_code}", response_model=ProductDB)
async def get_product(product_code: str):
    product = await crud.get_at("products", product_code)
    return product