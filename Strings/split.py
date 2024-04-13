s = "Python is fun"
l = s.split()
s_new = "-".join([l[0].upper(), l[1], l[2].capitalize()])
print(s_new)