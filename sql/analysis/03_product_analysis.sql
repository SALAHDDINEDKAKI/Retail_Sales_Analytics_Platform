SELECT
    product,
    SUM(operating_profit) AS profit
FROM fact_sales
GROUP BY product
ORDER BY profit DESC
LIMIT 10;