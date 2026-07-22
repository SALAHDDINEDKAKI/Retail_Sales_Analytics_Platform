CREATE TABLE sales (

    sale_id SERIAL PRIMARY KEY,
    retailer VARCHAR(100),
    retailer_id INTEGER,
    invoice_date DATE,
    region VARCHAR(50),
    state VARCHAR(50),
    city VARCHAR(100),
    product VARCHAR(100),
    price_per_unit NUMERIC(10,2),
    units_sold INTEGER,
    total_sales NUMERIC(12,2),
    operating_profit NUMERIC(12,2),
    operating_margin NUMERIC(5,2),
    sales_method VARCHAR(50),
    year INTEGER,
    month INTEGER,
    day INTEGER
);