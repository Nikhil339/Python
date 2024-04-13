import mysql.connector as sql
db = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@betterthanexcel95',
    database = 'courier_management'
)
mycursor = db.cursor() 

def table():
    print("----------WELCOME TO COURIER MANAGEMENT----------")
    print()
    while True:
        print("Select Any One Option: ")
        print("1. Packages", "2. Sender Info", "3. Receiver Info", "4. Exit", sep='\n')
        option = int(input("Your Entry: "))
        if option == 1:
            print()
            packages()
            print()
        elif option == 2:
            print()
            sender()
            print()
        elif option == 3:
            print()
            receiver()
            print()
        elif option == 4:
            break
        else:
            print("Invalid Option!")
            break


def packages():
    print("Select Any One Option: ", "1. Add Data", "2. View Data", "3. View Specific Record Using PID", "4. Delete Record", "5. Main Menu", sep="\n")
    option = int(input("Your Entry: "))
    print()
    if option == 1:
        type = input("Enter Package Type: ")
        mass = input("Enter Package Mass: ")
        sid = int(input("Enter Sender ID: "))
        rid = int(input("Enter Receiver ID: "))
        data = (type, mass, sid, rid)
        querry = "INSERT INTO packages (Type, Weight, SID, RID) VALUES (%s,%s,%s,%s)"
        mycursor.execute(querry, data)
        db.commit()
        print("Data Entered Successfully!")
    elif option == 2:
        mycursor.execute("SELECT * FROM packages")
        f = mycursor.fetchall()
        for x in f:
            print(x[0], x[1], x[2], x[3], x[4], sep=" <--> ")
    elif option == 3:
        pid = int(input("Enter the PID: "))
        mycursor.execute("SELECT * FROM packages WHERE PID = (%s)", (pid,))
        f = mycursor.fetchall()
        for x in f:
            print(x[0], x[1], x[2], x[3], x[4], sep=" <--> ")
    elif option == 4:
        pid = int(input("Enter the PID: "))
        mycursor.execute("DELETE FROM packages WHERE PID = (%s)", (pid,))
    elif option == 5:
        table()
    else:
        print("Invalid Input!")
        table()


def sender():
    print("Select Any One Option: ", "1. Add Data", "2. View Data", "3. View Specific Record Using SID", "4. Delete Record", "5. Main Menu", sep="\n")
    option = int(input("Your Entry: "))
    print()
    if option == 1:
        sid = int(input("Enter Sender ID: "))
        name = input("Enter Name: ")
        add = input("Enter Address: ")
        pnum = int(input("Enter Phone Number: "))
        data = (sid, name, add, pnum)
        querry = "INSERT INTO sender VALUES (%s,%s,%s,%s)"
        mycursor.execute(querry, data)
        db.commit()
        print("Data Entered Successfully!")
    elif option == 2:
        mycursor.execute("SELECT * FROM sender")
        f = mycursor.fetchall()
        for x in f:
            print(x[0], x[1], x[2], x[3], sep=" <--> ")
    elif option == 3:
        sid = input("Enter the SID: ")
        mycursor.execute("SELECT * FROM sender WHERE SID = (%s)", (sid,))
        f = mycursor.fetchall()
        for x in f:
            print(x[0], x[1], x[2], x[3], sep=" <--> ")
    elif option == 4:
        sid = int(input("Enter the SID: "))
        mycursor.execute("DELETE FROM sender WHERE SID = (%s)", (sid,))
    elif option == 5:
        table()
    else:
        print("Invalid Input!")
        table()


def receiver():
    print("Select Any One Option: ", "1. Add Data", "2. View Data", "3. View Specific Record Using RID", "4. Delete Record", "5. Main Menu", sep="\n")
    option = int(input("Your Entry: "))
    print()
    if option == 1:
        rid = int(input("Enter Receiver ID: "))
        name = input("Enter Name: ")
        add = input("Enter Address: ")
        pnum = int(input("Enter Phone Number: "))
        data = (rid, name, add, pnum)
        querry = "INSERT INTO receiver VALUES (%s,%s,%s,%s)"
        mycursor.execute(querry, data)
        db.commit()
        print("Data Entered Successfully!")
    elif option == 2:
        mycursor.execute("SELECT * FROM receiver")
        f = mycursor.fetchall()
        for x in f:
            print(x[0], x[1], x[2], x[3], sep=" <--> ")
    elif option == 3:
        rid = int(input("Enter the RID: "))
        mycursor.execute("SELECT * FROM receiver WHERE RID = (%s)", (rid,))
        f = mycursor.fetchall()
        for x in f:
            print(x[0], x[1], x[2], x[3], sep=" <--> ")
    elif option == 4:
        rid = int(input("Enter the RID: "))
        mycursor.execute("DELETE FROM receiver WHERE RID = (%s)", (rid,))
    elif option == 5:
        table()
    else:
        print("Invalid Input!")
        table()

try:
    table()
except sql.Error as e:
    print(f"Database error: {e}")
finally:
    db.close()
