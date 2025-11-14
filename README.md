
# Diligent Internship Task – COMPLETED PROJECT

## ✔️ Contents
This project fully completes the assignment:
1. Synthetic E‑commerce data (5 CSV files)
2. SQLite database ingestion
3. SQL JOIN query joining all tables

## ✔️ Files Included
- customers.csv  
- products.csv  
- orders.csv  
- order_items.csv  
- inventory.csv  
- ecom.sqlite  
- build_db.py  
- README.md

## ✔️ SQL JOIN Query (copy/paste)
```
SELECT o.order_id, o.order_date, o.status, o.total_amount,
       c.customer_id, c.first_name || ' ' || c.last_name AS customer_name, c.email,
       oi.order_item_id, oi.quantity, oi.unit_price, oi.subtotal,
       p.product_id, p.name AS product_name, p.category,
       inv.stock_qty, inv.warehouse
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
LEFT JOIN inventory inv ON p.product_id = inv.product_id
ORDER BY o.order_date DESC
LIMIT 100;
```

## ✔️ How to Use
Just upload all files into your GitHub repository.
