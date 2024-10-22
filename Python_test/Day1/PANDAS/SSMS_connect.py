import pyodbc
import pandas as pd

servername = 'amrt-ey-sqlserver.database.windows.net'
dbname ='sqlserverdb'
username = 'sqladmin'
password = 'Welcome@123'
connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+servername+';DATABASE='+dbname+';UID='+username+';PWD='+password)

df = pd.read_sql_query("SELECT Name, ListPrice from SalesLT.Product order by ListPrice desc, name",connection)

# df_sum = df.aggregate(["sum"])
# print(df_sum)

print(df)