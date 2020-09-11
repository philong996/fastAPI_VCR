from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class TransactionSchema(BaseModel):
    trans_code : str
    customer_id : int
    product_id : int
    promotion_code : Optional[str]
    price : Optional[int]
    discount : Optional[float]
    diamond_code : Optional[list]
    discount_diamond : Optional[float]
    price_diamond : Optional[list] 
    source : Optional[str] 
    store : str
    created_date: date

class TransactionDB(TransactionSchema):
    id : int

class CustomerSchema(BaseModel):
    customer_code : str
    gender : Optional[str]
    birthday : Optional[date]
    district : Optional[str]
    city : Optional[str]
    email : Optional[str]
    first_purchase_date : Optional[date]

class CustomerDB(CustomerSchema):
    id : int

class ProductSchema(BaseModel):
    product_code: str
    category: Optional[str]
    design_group: Optional[str]
    price_segment: Optional[str]
    size_diamond: Optional[str]

class ProductDB(ProductSchema):
    id : int