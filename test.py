print("Now reading the contents of the file: ")
object=open("3.txt","r")
str = object.readline().strip()
while str:
    print(str)
    str = object.readline().strip()
object.close()
