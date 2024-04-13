'''
NOTE:
file.mode() is used to know the mode in which the file is opened.
'''

with open('3.txt', 'r') as file:
    for line in file:
        print(line.split())

with open('3.txt', 'r') as file:
    for line in file:
        print(line.splitlines())
