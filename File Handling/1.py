file = open("1.txt", 'r')

content = file.read()
print(content.strip())

#to see the current position of the cursor
print(file.tell()) 
#after each read function the cursor moves to the end, after which there is no content.
file.seek(0)

line = file.readlines() #returns a list of the lines 
print(line)

file.seek(0) #moves the cursor to the beginning of the file.

line1 = file.readline()
line2 = file.readline().rstrip() #rstrip is used to remove the extra blank line at the end of the output.

print(f"{line1}{line2}")

file.close()

'''
print("Now reading the contents of the file: ")
fobject=open("3.txt","r")
for str in fobject:
    print(str.strip())
fobject.close()
'''