print("Now reading the contents of the file: ")
fobject=open("3.txt","r")
str = fobject.readline().strip()
while str:
    print(str)
    str = fobject.readline().strip()
fobject.close()