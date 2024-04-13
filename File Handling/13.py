#Creating a Binary File and using Pickle Module
'''
Creating a employee table:
1. Taking in the data(dumping the data)
2. Calculating the size of the binary file
3. Printing the entered data(loading the data)
'''
import pickle
import os 

os.chdir("File Handling")

bfile = open('empfile.dat', 'ab')
recno = 1

print("Enter the records of employees: \n")

while True:
    print("Record No.", recno)
    eno = int(input("\tEmployee number: "))
    ename = input("\tEmployee Name: ")
    ebasic = int(input("\tBasic Salary: "))
    allow = int(input("\tAllowances: "))
    totsal = ebasic+allow
    print(f"\tTotal Salary: {totsal}")
    edata = [eno, ename, ebasic, allow, totsal]
    pickle.dump(edata, bfile)

    ans = input("Do you want to add more records?(Y/N): ")
    recno += 1
    if ans.lower() == 'n':
        print("Done!\n")
        break

print("Size of binary file:", bfile.tell())
bfile.close()

print("\nDisplaying the records: ")
readrec = 1
try:
    with open('empfile.dat', 'rb') as bfile:
        while True:
            edata = pickle.load(bfile)
            print("Record No.", readrec)
            print(edata)
            readrec += 1
except EOFError:
    pass