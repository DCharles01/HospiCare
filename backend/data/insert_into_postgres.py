from data.pyspark_content import spark


parquet_file_path = 'path/to/your/parquet/file.parquet'
parquet_df = spark.read.parquet(parquet_file_path)

# Replace 'your_table_name' with the actual name you want for the temporary table
temporary_table_name = 'your_table_name'

parquet_df.write \
   .format("jdbc") \
   .option("url", "jdbc:postgresql://your_host:your_port/your_database_name") \
   .option("dbtable", temporary_table_name) \
   .option("user", "your_username") \
   .option("password", "your_password") \
   .mode("overwrite") \
   .save()

# Replace 'your_table_name' with the actual name of your target table
target_table_name = 'your_table_name'

spark.sql(f"INSERT INTO {target_table_name} SELECT * FROM {temporary_table_name}")

parquet_file_path_list = ['admission_sources', 'admission_types', 'diagnoses', 'discharge_depositions', 'insurances', 'medications', 'medication_changes', 'physicians', 'patients', 'readmissions', 'admissions', 'admission_procedures', 'lab_results']
def insert_into_postgres_table(parquet_file_path: str, host, port, dbname, user, password, temp_tbl_name):

    table_name = parquet_file_path
    parquet_df.write \
        .format("jdbc") \
        .option("url", f"jdbc:postgresql://your_host:your_port/your_database_name") \
        .option("dbtable", temporary_table_name) \
        .option("user", user) \
        .option("password", password) \
        .mode("overwrite") \
        .save()

