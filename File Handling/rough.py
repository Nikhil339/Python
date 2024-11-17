filename = '1.txt' 

lines = []
with open(filename, 'r') as file:
    for line in file:
        lines.append(line.strip())

print("The lines stored in the array are:")
print(lines)
