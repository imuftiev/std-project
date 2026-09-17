from airflow.sdk import DAG


with DAG (
    dag_id="controlflow",
    description="Управляющий поток",
    catchup=False,
    schedule=None
) as dag:

    @task
    def log_hello() -> None:
        print("Hello!")

    @task
    def log_info() -> None:
        print("Info")

    log_hello >> log_info