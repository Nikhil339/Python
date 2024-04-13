import pickle 
stu = {}
stufile = open('stu.dat','wb') #use 'ab' instead of 'wb' for appending more records later
ans = 'y'
while ans =='y':
    rno = int(input("Enter Roll Number: "))
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    stu["Rollno"] = rno
    stu["Name"] = name
    stu["Marks"] = marks
    pickle.dump(stu, stufile)
    ans = input("Want to add more records? (y/n)...")
stufile.close()
                