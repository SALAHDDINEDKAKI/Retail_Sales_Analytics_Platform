SELECT
    state,
    SUM(total_sales) AS revenue
FROM fact_sales
GROUP BY state
ORDER BY revenue DESC
LIMIT 10;