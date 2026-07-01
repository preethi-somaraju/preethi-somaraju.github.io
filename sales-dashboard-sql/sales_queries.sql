-- Business Reporting SQL Queries

-- 1. Monthly Revenue & Growth Trend
SELECT 
    strftime('%Y-%m', date) AS sales_month,
    ROUND(SUM(revenue), 2) AS monthly_revenue,
    COUNT(transaction_id) AS total_orders,
    ROUND(SUM(revenue) - LAG(SUM(revenue)) OVER (ORDER BY strftime('%Y-%m', date)), 2) AS mom_revenue_change
FROM sales_transactions
GROUP BY sales_month;

-- 2. Top Performing Product Categories
SELECT 
    product_category,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(revenue), 2) AS total_sales_revenue,
    ROUND((SUM(revenue) / (SELECT SUM(revenue) FROM sales_transactions)) * 100, 2) AS sales_percentage
FROM sales_transactions
GROUP BY product_category
ORDER BY total_sales_revenue DESC;

-- 3. Top High-Value Customers (VIPs)
SELECT 
    customer_id,
    COUNT(transaction_id) AS orders_placed,
    ROUND(SUM(revenue), 2) AS total_spend
FROM sales_transactions
GROUP BY customer_id
ORDER BY total_spend DESC
LIMIT 10;
