from app.api.models import TransactionSchema
from app.db import database, transactions, products, customers

async def insert_customer(payload: CustomerSchema):
    query = customers.insert().values(customer_code = payload.customer_code,
                                      gender = payload.gender,
                                      birthday = payload.birthday,
                                      district = payload.district,
                                      city = payload.city,
                                      email = payload.email,
                                      first_purchase_date = payload.first_purchase_date)
    return await database.execute(query=query)