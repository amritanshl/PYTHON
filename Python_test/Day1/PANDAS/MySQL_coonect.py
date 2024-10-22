import mysql.connector

config ={

    'host':'amrit-ey-mysql.mysql.database.azure.com',
    'user':'sqladmin',
    'password':'Welcome@123',
    'database':'mysql'

}

try:
    connection = mysql.connector.connect(**config)
    print("successfully connected!! ")
except Exception:
    print("Not connected ")