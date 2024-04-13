n = int(input("Enter a number: "))
x = 0 

for i in range(1,n+1):
    if n%i == 0:
        x += 1

if x == 2:
    print("Prime Number")
elif x == 1:
    print("Special Number")
else:
    print("Not Prime")