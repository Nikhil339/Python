import pickle 
stu = {}
fin = open('stu.dat','rb')
try:
    print("file stu.dat stores these records")
    while True:
        stu = pickle.load(fin)
        print(stu)
except EOFError:
    fin.close()