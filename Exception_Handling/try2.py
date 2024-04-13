print("leraning try and except!")
try:
    x = int(input("Enter a number: ")) #put x = any float
    y = 50
    z = y/x
except ZeroDivisionError as e:
    print(f"Denominator is zero dude: {e}")
else:
    print(f"The quotient is {z}")
finally:
    print("TEST") #as there is no handler for ValueError the error will raised after the execution of finally block
print("Done!") #this will not be performed
