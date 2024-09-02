s1 = set()
s2 = set()
s3 = set()

print("Enter elements for set 1: ")
for _ in range(0,10):
    ip = int(input("Enter element: "))
    s1.add(ip)
print(s1)

print("Enter elements for set 2: ")
for _ in range(0,10):
    ip = int(input("Enter element: "))
    s2.add(ip)
print(s2)

print("Enter elements for set 3: ")
for _ in range(0,10):
    ip = int(input("Enter element: "))
    s3.add(ip)
print(s3)

#checking for common elements
if s1.isdisjoint(s2) and s2.isdisjoint(s3) and s3.isdisjoint(s1):
    print("There are no common elements between the three sets!")
else:
    print("There are common elemnts between the three sets.")

#removing common elements
z = s1.intersection(s2, s3)
s1 = s1 - z
s2 = s2 - z
s3 = s3 - z

print(s1,s2,s3, sep="\n")
