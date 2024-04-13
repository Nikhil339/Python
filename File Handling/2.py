file = open('1.txt', 'w')
write = file.write("This is the 1st line written using write function.")
file.close() #using the write function we can also create files

file = open('1.txt', 'r')
read = file.read()
print(read)
file.close()

file = open('1.txt','a') #using the append function to add new content
new = file.write("\nThis is the 2nd line.\n")
file.close()

file = open('1.txt', 'r')
read = file.read()
print(read)
file.close()
