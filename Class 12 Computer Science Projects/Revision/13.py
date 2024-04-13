num = int(input("Enter any number: "))
fact = 1 
n = num
while num>1:
    fact = fact*num
    num -= 1

print("Factorial of", n,"is:", fact)