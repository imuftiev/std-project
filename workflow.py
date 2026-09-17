from airflow.sdk import DAG


with DAG (
    dag_id= "demo_workflow",
    description= "Тестовый рабочий поток",
    catchup=False,
    schedule=None
) as dag:
    
    @task
    def get_users() -> None:
        hook = PostgresHook (
            postgres_conn_id= "date-bot"
        )

        records = hook.get_records(
            "SELECT * FROM users;"
        )

        print(dict(records))
        
    get_users()