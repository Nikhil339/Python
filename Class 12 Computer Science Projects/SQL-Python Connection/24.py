import mysql.connector as sql

db = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@betterthanexcel95',
    database = 'employee'
)

mycursor = db.cursor()

eid = int(input("Enter the EMPID of the employee to view their record: "))

mycursor.execute("SELECT * FROM employee WHERE EMPID = (%s)", (eid,))

d = mycursor.fetchall()

for i in d:
    print(i[0], i[1], i[2], i[3], i[4], i[5], sep=" --- ")

db.close()

