import os

from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table, Date, create_engine, ForeignKey, Float

from sqlalchemy.sql import func

from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy connection
engine = create_engine(DATABASE_URL)
metadata = MetaData()

transactions = Table(
    "transactions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("trans_code", String(16)),
    Column("customer_id", Integer, ForeignKey("customers.id"),nullable=False),
    Column("product_id", Integer, ForeignKey("products.id"), nullable=False),
    Column("promotion_code", String(16)),
    Column("price", Integer, nullable=False),
    Column("discount", Float),
    Column("source", String(16)),
    Column("store",String(16)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_code", String(16), nullable=False),
    Column("category", String(16)),
    Column("design_group", String(16)),
    Column("price_segment", String(8))
)

customers = Table(
    "customers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("customer_code", String(16), nullable=False),
    Column("gender", String(8)),
    Column("birthday", Date),
    Column("district", String(16)),
    Column("city", String(32)),
    Column("email", String),
    Column("first_purchase_date", Date)
)

# databases query builder
database = Database(DATABASE_URL)