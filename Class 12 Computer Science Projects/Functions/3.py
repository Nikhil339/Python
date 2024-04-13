def fiboterm(n):
    if n<=1:
        return n
    else:
        return (fiboterm(n-1)+fiboterm(n-2))
    
num = int(input("Enter the n term to find in fibonacci: "))
term = fiboterm(num)
print(num, "th term of fibonacci series is:", term)