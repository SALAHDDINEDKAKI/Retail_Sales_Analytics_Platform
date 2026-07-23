SELECT
    sales_method,
    SUM(total_sales) AS revenue,
    SUM(operating_profit) AS profit,
    COUNT(*) AS transactions
FROM fact_sales
GROUP BY sales_method
ORDER BY revenue DESC;