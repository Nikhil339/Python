import mysql.connector as sql

db = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@betterthanexcel95',
)

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS employee")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
