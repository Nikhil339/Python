def bubble(list):
    n = len(list)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if list[j]>list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    print(list)

test = [1,4,3,2,4,5,8,9,5,7,43,1]
bubble(test)