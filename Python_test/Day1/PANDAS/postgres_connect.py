import psycopg2

servername =''
dbname =''
user=''
password = ''
connectionString = "host="+servername+" user="+user +" password="+password+" sslmode=require"
conn = psycopg2.connect(connectionString)
cox = conn.cursor()

cox.execute("<write your query>")
conn.commit()
cox.close()