def push(list, length):
    for i in range(length):
        value = input(f"Enter the {i+1} data item: ")
        if value.isdigit() == True:
            value = int(value)
            list.append(value)
        else:
            list.append(value)

def empty(list):
    if len(list) == 0:
        return True
    else:
        return False
    
def pop(list):
    if empty(list):
        print("Underflow!")
    else:
        list.pop()

def top(list):
    if empty(list):
        print("Stack is empty")
    else:
        x = len(list)
        return list[x-1]
    
def select():
    
    while True:
        user = int(input("Please select from the following options: \n1.Add\n2.Remove\n3.View Top Element\n4.Exit\n"))
        match user:
            case 1:
                push(stack, max)
            case 2:
                pop(stack)
            case 3:
                print(top(stack))
            case 4:
                break


max = int(input("How many data items do you want in your stack: "))
stack = []

select()





