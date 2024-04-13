'''
file = open('5.txt','w')
file.write("Hello")
file.write("\nSenorita")
'''

file = open('5.txt','r')
content = file.read()
print(content)

file.seek(0)

single = file.readlines()
for line in single:
    if line.startswith("S"):
        print(line.strip())

file.close()
