print("leraning try and except!")
try:
    x = int(input("Enter a number: "))
    y = 50
    z = y/x
except ZeroDivisionError as e:
    print(f"Denominator is zero dude: {e}")
except ValueError as e:
    print(f"Yo, please use integers: {e}")
except:
    print("Some random error popped up!")
else:
    print(f"The quotient is {z}")
finally:
    print("Something")
print("Done!")
