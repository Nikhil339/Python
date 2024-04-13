file = open('2.txt', 'w')
write = file.write('Writing something so that I can practice file handling using python.')
file.close()

file = open('2.txt','r')
read = file.read()
print(read)
file.close()

file = open('2.txt','a')
append = file.write("\nAdding something!")
file.close()

file = open('2.txt','r')
read = file.read()
print(read)
file.close()
