SELECT
    retailer,
    SUM(operating_profit) AS profit
FROM fact_sales
GROUP BY retailer
ORDER BY profit DESC;