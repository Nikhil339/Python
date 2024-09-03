numb = [1, 2, 3, 4, 5]
print(*numb)

def pizzorder(size, *toppings, **notes): 
    print(f"Size: {size}")
    
    if toppings:
        print("Toppings: ", end="")
        print(", ".join(toppings))
    else:
        print("Toppings: None")
    
    if notes:
        print("Notes: ")
        for key, value in notes.items():
            print(f"  {key}: {value}")
    else:
        print("Notes: None")

pizzorder("large", "onion", "capsicum", delivery=True, tips=15)
