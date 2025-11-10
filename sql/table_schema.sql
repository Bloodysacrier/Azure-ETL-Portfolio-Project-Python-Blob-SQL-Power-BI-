/* ===========================
   DIM CUSTOMER
   =========================== */
CREATE TABLE dbo.dim_customer (
    customer_key INT IDENTITY(1,1) PRIMARY KEY,
    customer_id VARCHAR(50),
    customer_name VARCHAR(255),
    segment VARCHAR(100)
);


/* ===========================
   DIM PRODUCT
   =========================== */
CREATE TABLE dbo.dim_product (
    product_key INT IDENTITY(1,1) PRIMARY KEY,
    product_id VARCHAR(50),
    category VARCHAR(100),
    sub_category VARCHAR(100),
    product_name VARCHAR(255)
);


/* ===========================
   DIM ORDER
   =========================== */
CREATE TABLE dbo.dim_order (
    order_key INT IDENTITY(1,1) PRIMARY KEY,
    order_id NVARCHAR(50),
    order_date_key INT,
    ship_date_key INT
);


/* ===========================
   DIM SHIPPING
   =========================== */
CREATE TABLE dbo.dim_shipping (
    shipping_key INT IDENTITY(1,1) PRIMARY KEY,
    ship_mode VARCHAR(100)
);


/* ===========================
   DIM LOCATION
   =========================== */
CREATE TABLE dbo.dim_location (
    location_key INT IDENTITY(1,1) PRIMARY KEY,
    country VARCHAR(100),
    state VARCHAR(100),
    city VARCHAR(100),
    region VARCHAR(100)
);


/* ===========================
   DIM DATE
   =========================== */
CREATE TABLE dbo.dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE,
    year INT,
    month INT,
    day INT
);


/* ===========================
   FACT SALES
   =========================== */
CREATE TABLE dbo.fact_sales (
    sales_key INT IDENTITY(1,1) PRIMARY KEY,

    order_key INT,
    customer_key INT,
    product_key INT,
    shipping_key INT,
    location_key INT,

    sales DECIMAL(18,2),
    quantity INT,
    discount DECIMAL(10,2),
    profit DECIMAL(18,2),
    profit_ratio DECIMAL(10,4),

    order_id NVARCHAR(50),
    product_id VARCHAR(50),
    customer_id VARCHAR(50)
);


/* ===========================
   FOREIGN KEYS
   =========================== */

ALTER TABLE dbo.fact_sales
ADD CONSTRAINT fk_sales_order
FOREIGN KEY (order_key) REFERENCES dbo.dim_order(order_key);

ALTER TABLE dbo.fact_sales
ADD CONSTRAINT fk_sales_customer
FOREIGN KEY (customer_key) REFERENCES dbo.dim_customer(customer_key);

ALTER TABLE dbo.fact_sales
ADD CONSTRAINT fk_sales_product
FOREIGN KEY (product_key) REFERENCES dbo.dim_product(product_key);

ALTER TABLE dbo.fact_sales
ADD CONSTRAINT fk_sales_shipping
FOREIGN KEY (shipping_key) REFERENCES dbo.dim_shipping(shipping_key);

ALTER TABLE dbo.fact_sales
ADD CONSTRAINT fk_sales_location
FOREIGN KEY (location_key) REFERENCES dbo.dim_location(location_key);



