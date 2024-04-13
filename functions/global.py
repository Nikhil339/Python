'''
global variables i.e variable outside the function can be accessed inside a function but cannot 
change/modify its value inside a function for which we have to use 'global' keyword
'''

b = 100
def test(a):
    global b
    b = b+a
    print(a,b)
test(10)
print(b)