--rule: check_duplicate_customer_email
--purpose: Ensure customer_email values are unique for each customer

SELECT
    customer_email,
    COUNT(*) AS duplicate_count
FROM customers
GROUP BY customer_email
HAVING COUNT(*) > 1;