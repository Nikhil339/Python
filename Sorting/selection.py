def selection(list):
    flag = 0 
    n = len(list)
    for i in range(0,n-1):
        min = i
        for j in range(i+1, n):
            if list[j]<list[min]: #change the inequality for descending order
                min = j
                flag = 1
        if flag == 1:
            list[min], list[i] = list[i], list[min]

l = [87, -55, 31, 68, -12, 42, 5, -76, 92, 20]
selection(l)
for _ in range(len(l)):
    print(l[_], end = " ")