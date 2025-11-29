> Create a bucket
shell
```
    gsutil mb gs://sql-dw-course-analystihas/
```

> Install Gcloud CLI
https://cloud.google.com/sdk/docs/install


> Send File to Bucket
```
gsutil cp "C:/Users/DELL/OneDrive/Documentos/projetos/sql-datawarehouse/datasets/source_crm/cust_info.csv" gs://sql-dw-course-analystihas/

```

> Builk insert in table
```
bq load --source_format=CSV --skip_leading_rows=1 sql-dw-course:bronze.crm_cust_info gs://sql-dw-course-analystihas/cust_info.csv


```