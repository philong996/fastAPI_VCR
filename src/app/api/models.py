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
    created_date: datetime

class CustomerSchema(Base):
    customer_code : str
    gender : str
    birthday : str
    district : str
    city : str
    email : str
    first_purchase_date : datetime

class CustomerDB(CustomerSchema):
    id : int