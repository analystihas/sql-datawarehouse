import os
from dotenv import load_dotenv
from google.cloud import bigquery

def load_csv_to_bigquery(
    project_id: str,
    dataset_id: str,
    table_id: str,
    csv_path: str
):
    # Carrega as variáveis do .env
    load_dotenv()

    # Seta credenciais
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("SECRET_PATH")

    client = bigquery.Client(project=project_id)

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,  # Auto-schema
        write_disposition="WRITE_TRUNCATE"  # sobrescreve a tabela
    )

    # Abre o CSV local
    with open(csv_path, "rb") as file_obj:
        load_job = client.load_table_from_file(
            file_obj,
            table_ref,
            job_config=job_config
        )

    print("Carregando dados...")
    load_job.result()  # Espera o job terminar

    table = client.get_table(table_ref)
    print(f"Carregado com sucesso! {table.num_rows} linhas na tabela {table_ref}")


