from app.api.models import TransactionSchema, CustomerSchema, ProductSchema
from app.db import database, transactions, products, customers
from datetime import date, datetime

async def insert_customer(payload: CustomerSchema):
    query = customers.insert().values(customer_code = payload.customer_code,
                                      gender = payload.gender,
                                      birthday = payload.birthday,
                                      district = payload.district,
                                      city = payload.city,
                                      email = payload.email,
                                      first_purchase_date = payload.first_purchase_date)
    return await database.execute(query=query)

async def insert_product(payload: ProductSchema):
    query = products.insert().values(product_code = payload.product_code,
                                    category = payload.category,
                                    design_group = payload.design_group,
                                    price_segment = payload.price_segment)
    return await database.execute(query=query)


async def insert_transaction(payload: TransactionSchema):
    query = transactions.insert().values(trans_code = payload.trans_code,
                                    customer_id = payload.customer_id,
                                    product_id = payload.product_id,
                                    promotion_code = payload.promotion_code,
                                    price = payload.price,
                                    discount = payload.discount,
                                    source = payload.source,
                                    store = payload.store,
                                    created_date = payload.created_date)
    return await database.execute(query=query)