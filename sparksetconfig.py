
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
.config("spark.app.name", "testing") \
.config("spark.master", "local[*]") \
.config("spark.executor.instances", "3") \
.config("spark.executor.cores", "3") \
.config("spark.executor.memory", "40g") \
.config("spark.driver.memory", "2g") \
.config("spark.driver.cores", "1") \
.getOrCreate()

df = spark.read \
.option("recursiveFileLookup","true") \
.csv("/user/abhisek/files/")

result = df.filter(col("_c1").contains("PAYMENT"))

configurations = spark.sparkContext.getConf().getAll()
for conf in configurations:
    print(conf)
