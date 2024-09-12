n = 10

num1 = 0
num2 = 1
num = 0

for i in range(n+1):
    num = num1 + num2
    print(num, end = " ")
    num1, num2 = num2, num


