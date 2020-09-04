from pydantic import BaseModel
from datetime import date, datetime

class TransactionSchema(BaseModel):
    trans_code : str
    customer_id : int
    product_id : int
    promotion_code : str
    price : int
    discount : float
    diamond_code : str
    discount_diamond : float
    price_diamond : str 
    source : str 
    store : str
    created_date: date

class TransactionDB(TransactionSchema):
    id : int

class CustomerSchema(BaseModel):
    customer_code : str
    gender : str
    birthday : date
    district : str
    city : str
    email : str
    first_purchase_date : date

class CustomerDB(CustomerSchema):
    id : int

class ProductSchema(BaseModel):
    product_code: str
    category: str
    design_group: str
    price_segment: str
    size_diamond: str

class ProductDB(ProductSchema):
    id : int