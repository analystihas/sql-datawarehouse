from transfer_data_to_bq import load_csv_to_bigquery
import time


database_files = {
    "crm_cust_info":"cust_info", 
    "crm_sales":"sales_details",
    "crm_prd_info":"prd_info",
    "erp_cust_az12":"CUST_AZ12",
    "erp_loc_a101": "LOC_A101",
    "erp_px_cat_g1v2":"PX_CAT_G1V2"
}

global_start = time.perf_counter()

for table, file in database_files.items():
    if "crm" in table:
        csv_path = f"../datasets/source_crm/{file}.csv"
    else:
        csv_path = f"../datasets/source_erp/{file}.csv"

    start = time.perf_counter()
    
    load_csv_to_bigquery(
        project_id="sql-dw-course",
        dataset_id="bronze",
        table_id=table,
        csv_path=csv_path
    )

    duration = time.perf_counter() - start
    print(f"Insert '{table}' concluded in {duration:.2f} seconds")

global_duration = time.perf_counter() - global_start

print(f"\nBronze Layer data load concluded in {global_duration:.2f} seconds")
