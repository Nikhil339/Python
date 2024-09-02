from statistics import mean

list1 = []
list2 = []

print("Enter elements for list1: ")
for _ in range(0,10):
    ip = int(input("Enter element: "))
    list1.append(ip)
print(list1)

print("Enter elements for list2: ")
for _ in range(0,10):
    ip = int(input("Enter element: "))
    list2.append(ip)
print(list2)

#sorting lists
list1.sort()
print("\n Sorted list1:", list1)
list2.sort()
print("\n Sorted list2:", list2)

list3 = list1 + list2
list3.sort()
print("\n Sorted list3:", list3)

#removing duplicate elements
s = set(list3)
list4 = list(s)
print("\nRemoving duplicate elements:", list4)
print("\nSum of the list is:", sum(list4))
print("\nAverage of the list is:", mean(list4))

#removing zero and negative numbers from the list
positive_list = []
for i in list4:
    if i>0:
        positive_list.append(i)
    else:
        continue
print("\nUpdated List:", positive_list)

#storing even and odd numbers in separate lists
evlist = []
odlist = []

for i in positive_list:
    if i%2 == 0:
        evlist.append(i)
    else:
        odlist.append(i)

print("\nEven list of numbers:", evlist)
print("\nOdd list of numbers:", odlist)
