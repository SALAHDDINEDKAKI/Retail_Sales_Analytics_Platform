SELECT
    retailer,
    SUM(total_sales) AS revenue,
    SUM(operating_profit) AS profit,
    AVG(operating_margin) AS avg_margin
FROM fact_sales
GROUP BY retailer
ORDER BY revenue DESC;