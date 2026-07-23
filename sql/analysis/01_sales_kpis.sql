-- Total Revenue
SELECT
    SUM(total_sales) AS total_revenue
FROM fact_sales;


-- Total Profit
SELECT
    SUM(operating_profit) AS total_profit
FROM fact_sales;


-- Total Units Sold
SELECT
    SUM(units_sold) AS total_units
FROM fact_sales;


-- Average Operating Margin
SELECT
    AVG(operating_margin) AS avg_margin
FROM fact_sales;