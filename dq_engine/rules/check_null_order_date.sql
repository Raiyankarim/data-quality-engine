-- Rule: Check for NULL order_date values
-- Purpose: Ensure all orders have a valid order_date

SELECT
    COUNT(*) AS null_order_date_count
FROM orders
WHERE order_date IS NULL;