import mysql.connector as sql

db = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@betterthanexcel95',
    database = 'employee'
)

mycursor = db.cursor()

emp_data = [
    ('Aarav', 25, 'M', 60000, 'IT'),
    ('Sanya', 28, 'F', 75000, 'Engineering'),
    ('Rahul', 22, 'M', 50000, 'Marketing'),
    ('Neha', 30, 'F', 80000, 'Finance'),
    ('Vikram', 40, 'M', 90000, 'HR')
]

querry = "INSERT INTO employee(NAME, AGE, GENDER, SALARY, DEPARTMENT) VALUES (%s,%s,%s,%s,%s)"

for data in emp_data:
    mycursor.execute(querry, data)

db.commit()

mycursor.execute("SELECT * FROM employee")

for x in mycursor:
    print(x)

db.close()
