import os 
print(os.getcwd())

os.chdir('test')
file = open('test.txt', 'r')
inside = file.read()
print(inside)
file.close()
print(os.getcwd())

os.chdir(os.path.join('..','File Handling'))
print(os.getcwd())
print(os.listdir())

os.chdir('..')
print(os.getcwd())

'''
Here Python is the parent directory and to go from test folder to file handling folder you must return to the
parent directory and then move forward to fild handling directory.
'''