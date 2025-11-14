
import pandas as pd
import sqlite3

# Load CSVs
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")
order_items = pd.read_csv("order_items.csv")
inventory = pd.read_csv("inventory.csv")

# Create DB
conn = sqlite3.connect("ecom.sqlite")
cursor = conn.cursor()

# ---------------------------------------------------
# CREATE TABLES BEFORE INSERTING DATA
# ---------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    city TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items(
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    price REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory(
    product_id INTEGER,
    stock_available INTEGER
)
""")

# ---------------------------------------------------
# INSERT CSV DATA INTO TABLES
# ---------------------------------------------------

customers.to_sql("customers", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)
order_items.to_sql("order_items", conn, if_exists="replace", index=False)
inventory.to_sql("inventory", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("DATABASE READY ✔")
