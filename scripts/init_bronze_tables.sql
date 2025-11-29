CREATE TABLE IF NOT EXISTS bronze.crm_cust_info (
  cst_id INT64,
  cst_key STRING(50),
  cst_firstname STRING(50),
  cst_lastname STRING(50),
  cst_marital_status STRING(50),
  cst_gndr STRING(50),
  cst_create_date DATE
);

CREATE TABLE IF NOT EXISTS bronze.crm_prd_info (
  prd_id INT64,
  prd_key STRING(50),
  prd_nm STRING(50),
  prd_cost INT64,
  prd_line STRING(50),
  prd_start_dt DATETIME,
  prd_end_dt DATETIME
);

CREATE TABLE IF NOT EXISTS bronze.crm_sales_details (
  sls_ord_num STRING(50),
  sls_prd_key STRING(50),
  sls_cust_id INT64,
  sls_order_dt INT64,
  sls_ship_dt INT64,
  sls_due_dt INT64,
  sls_sales INT64,
  sls_quantity INT64,
  sls_price INT64
);

CREATE TABLE IF NOT EXISTS bronze.erp_loc_a101 (
    cid STRING(50),
    cntry STRING(50)
);

CREATE TABLE IF NOT EXISTS bronze.erp_cust_az12 (  
    cid STRING(50),
    bdate DATE,
    gen STRING(50)

);


CREATE TABLE IF NOT EXISTS bronze.erp_px_cat_g1v2 (
  id STRING(50),
  cat STRING(50),
  subcat STRING(50),
  maintenance STRING(50)
);