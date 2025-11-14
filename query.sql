SELECT 
    customers.name AS customer_name,
    products.name AS product_name,
    order_items.quantity,
    orders.order_date
FROM customers
JOIN orders ON customers.id = orders.customer_id
JOIN order_items ON orders.order_id = order_items.order_id
JOIN products ON order_items.product_id = products.id;

