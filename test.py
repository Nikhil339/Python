amount = 50

while amount != 0:
    print(f"Amount due: {amount}")
    insert =  int(input("Enter coin: "))
    match insert:
        case 25 | 10 | 5:
            if insert <= amount:
                amount -= insert
            else:
                continue
        case _:
            continue

print(f"Change owed: {amount}")