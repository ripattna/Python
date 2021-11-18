import pymysql
import pandas as pd
from pyspark.sql import SparkSession

# Creating the SparkSession
spark = SparkSession.builder.appName('Test').master("local").getOrCreate()

# Open database connection
dbcon = pymysql.connect(
    host="localhost",
    user="rissan",
    password="rissan",
    database="demo")

try:
    SQL_Query = pd.read_sql_query(
        '''select
          Id,
          Name,
          Gender,
          Salary
          from employee''', dbcon)

    pdf = pd.DataFrame(SQL_Query, columns=['Id', 'Name', 'Gender', "Salary"])
    print(pdf)
    print('The data type of pdf is: ', type(pdf))

    # Create a Spark DataFrame from a Pandas DataFrame
    df = spark.createDataFrame(pdf)
    print(df.show())
    print('The data type of df is: ', type(df))
    df.write.saveAsTable("default.employee")

    spark.sql("select * from default.employee").show()

    # df.createGlobalTempView("employee")
    df.createOrReplaceGlobalTempView("employee")
    spark.sql("select * from employee").show()


except:
    print("Error: unable to convert the data")

dbcon.close()

