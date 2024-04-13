def insertion(list):
    n = len(list)
    for i in range(n):
        temp = list[i]
        j = i-1
        while j>=0 and temp<list[j]:
            list[j+1]=list[j]
            j = j-1
        list[j+1] = temp

l = [87, -55, 31, 68, -12, 42, 5, -76, 92, 20]
insertion(l)
for i in range(len(l)):
    print(l[i], end=" ")