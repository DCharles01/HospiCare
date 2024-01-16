from pyspark.sql import SparkSession

# Create a Spark session with configurations
spark = (SparkSession.builder.appName("diabetic_app")
            .config("spark.executor.memory", "4g") 
            .config("spark.executor.cores", "4") 
            .config("spark.executor.instances", "2")
            .config("spark.driver.memory", "2g") 
            .config("spark.sql.shuffle.partitions", "200")
            .config("spark.default.parallelism", "200")
            .getOrCreate())