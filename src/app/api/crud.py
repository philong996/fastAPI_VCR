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
                                    price_segment = payload.price_segment,
                                    size_diamond = payload.size_diamond)
    return await database.execute(query=query)


async def insert_transaction(payload: TransactionSchema):
    query = transactions.insert().values(trans_code = payload.trans_code,
                                    customer_id = payload.customer_id,
                                    product_id = payload.product_id,
                                    promotion_code = payload.promotion_code,
                                    price = payload.price,
                                    discount = payload.discount,
                                    price_diamond = payload.price_diamond,
                                    discount_diamond = payload.discount_diamond,
                                    diamond_code = payload.diamond_code,
                                    source = payload.source,
                                    store = payload.store,
                                    created_date = payload.created_date)
    return await database.execute(query=query)

async def get_at(table, code):
    if table == "products":
        query = products.select().where(products.c.product_code == code)
        return await database.fetch_one(query)
    elif table == "customers":
        query = customers.select().where(customers.c.customer_code == code)
        return await database.fetch_one(query)
    else:
        return None

async def get_by_id(table, id):
    if table == "products":
        query = products.select().where(products.c.id == id)
        return await database.fetch_one(query)
    elif table == "customers":
        query = customers.select().where(customers.c.id == id)
        return await database.fetch_one(query)
    else:
        return None    