SELECT
    EXTRACT(YEAR FROM invoice_date) AS year,
    EXTRACT(MONTH FROM invoice_date) AS month,
    SUM(total_sales) AS revenue,
    SUM(operating_profit) AS profit
FROM fact_sales
GROUP BY
    year,
    month
ORDER BY
    year,
    month;