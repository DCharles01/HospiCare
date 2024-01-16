####################################################################################################################
# Airflow
airflow-yml-download:
	curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.0/docker-compose.yaml'

####################################################################################################################
# DBT
dbt-run:
	dbt run
dbt-tests:
	dbt test
dbt-debug:
	dbt debug

####################################################################################################################
# Set up cloud infrastructure

tf-init:
	terraform -chdir=./terraform init

tf-up:
	terraform -chdir=./terraform apply

tf-down:
	terraform -chdir=./terraform destroy

tf-config:
	terraform -chdir=./terraform output





