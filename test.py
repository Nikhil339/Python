list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

x = zip(list1, list2)
xl = list(x)

l = []

for i in xl:
    z = i[0] + i[1]
    l.append(z)

print(l)