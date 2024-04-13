file = open('3.txt','r')
content = file.read()
size = len(content)
print(f'size of the given text file is {size}')
file.seek(0)
content = file.readlines()
lines = len(content)
print(f'number of lines {lines}')
file.close()

'''
NOTE:
to check whether a particular file exists or not use
os.path.exists(file_path)
'''
