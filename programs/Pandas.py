import numpy as np
import pandas as pd
from pandasql import sqldf
import pandasql as ps
import openpyxl

# df1=pd.read_csv(filepath_or_buffer="C:\\Users\\india\\Downloads\\Contact_info1.csv")
# df2=pd.read_csv(filepath_or_buffer="C:/Users/india/Downloads/Contact_info1.csv")
# df3=pd.read_csv(r"C:\\Users\\india\\Downloads\\Contact_info1.csv",delimiter=',')
# print(df1.head(4))
# print(df2.head(4))
# print(df3.head(4))
# print(type(df3))
# pd.set_option('display.max_columns',None)
# pd.set_option('display.width',2000)
# print(df3.head(4))
# print(df3.shape[0], df3.shape[1])
# print(df3.shape)
# print(df3.columns)
# print(df3.dtypes)
# print(df3.describe())
# sdf=ps.sqldf("select * from df3")
# print(sdf)
# print(df3['Identifier'],['Surname'])
#
# dfexc =pd.read_excel(r"C:\Users\india\PycharmProjects\junebatch\files\Master_Test_Template.xlsx")
# print(dfexc.head(4))

# df4=pd.read_csv(r"C:\Users\india\PycharmProjects\junebatch\files\200records.csv")
# print(df4.head(5))
# pd.set_option('display.max_columns',None)
# pd.set_option('display.width',2000)
# df5=pd.read_excel(r"C:\Users\india\Desktop\ETL Testing\ETL Testing Automation\Srini\files\Master_Test_Template.xlsx")
# print(df5.head(4))
# # print(df5.iloc[0:3,1:3])
# print(df5[(df5.test_case_id > 2)])

#
# from pyspark.sql import SparkSession
# data=[(1,2)]
# schema=['col1','col2']
# spark=SparkSession.builder.getOrCreate()
# spark.createDataFrame(data=data,schema=schema).show()

from pyspark.sql import SparkSession
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkByExamples.com") \
      .getOrCreate()
dataList = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
df=spark.createDataFrame(dataList, schema=['Language','fee'])
df.show()