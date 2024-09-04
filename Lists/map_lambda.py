#lambda function is an anonymous function that is used in higher order function,
#i.e., to use a function inside a function,
#it is not callable like regular functions

def add(x,y):
    return x+y
print(add(1,2))

print((lambda x,y: x+y)(1,2))

a = [1,2,3,4,5]
b = list(map(lambda x: x**2, a)) #the map function maps each element in the list to the functoin lambda,
#useful instead of using for loops for applying the function to each element
print(b)