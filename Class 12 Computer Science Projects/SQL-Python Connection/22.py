import mysql.connector as sql

db = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@betterthanexcel95',
    database = 'employee'
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS employee(EMPID int PRIMARY KEY AUTO_INCREMENT, NAME varchar(20) NOT NULL, AGE int NOT NULL, GENDER ENUM('M', 'F', 'O') NOT NULL, SALARY int NOT NULL, DEPARTMENT varchar(20) NOT NULL)")

mycursor.execute("select * from employee")

for x in mycursor:
    print(x)

db.close()
