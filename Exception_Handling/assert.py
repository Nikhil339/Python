import math
def negativecheck(number):
    assert number>=0, "Negative Number!"

x = int(input("Please enter a number: "))
negativecheck(x)
print(math.sqrt(x))


