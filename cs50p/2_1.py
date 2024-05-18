camel = input("camelCase: ")
camells = []

for i in camel:
    if i.islower():
        camells.append(i)
    else:
        camells.append("_")
        camells.append(i)

print("snakeCase: ", end="")
for i in camells:
    print(i, end="")