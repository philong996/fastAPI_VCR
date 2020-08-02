from pydantic import BaseModel
from datetime import date, datetime

class TransactionSchema(BaseModel):
    trans_code : str
    trans_code : str
    customer_id : str
    product_id : str
    promotion_id : str
    store_id : str
    price : int
    discount : float 
    source : str 
    store : str
    created_date: str

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