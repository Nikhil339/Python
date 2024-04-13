import mysql.connector as sql

db = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@betterthanexcel95',
    database = 'employee'
)

mycursor = db.cursor()

eid = int(input("Enter the EMPID for which you want to delete record: "))

mycursor.execute("DELETE FROM employee WHERE EMPID = (%s)", (eid,))
db.commit()

mycursor.execute("SELECT * FROM employee")
for i in mycursor:
    print(i[0], i[1], i[2], i[3], i[4], i[5], sep=" --- ")

db.close()