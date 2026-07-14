-- ============================================================
-- Sales Table
-- ============================================================

CREATE TABLE IF NOT EXISTS sales (

    row_id INTEGER,

    order_id VARCHAR(30),

    order_date DATE,

    ship_date DATE,

    ship_mode VARCHAR(50),

    customer_id VARCHAR(30),

    customer_name TEXT,

    segment VARCHAR(30),

    country VARCHAR(50),

    city VARCHAR(50),

    state VARCHAR(50),

    postal_code INTEGER,

    region VARCHAR(20),

    product_id VARCHAR(30),

    category VARCHAR(50),

    sub_category VARCHAR(50),

    product_name TEXT,

    sales DOUBLE PRECISION,

    quantity INTEGER,

    discount DOUBLE PRECISION,

    profit DOUBLE PRECISION

);