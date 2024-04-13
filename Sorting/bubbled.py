def dbubble(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lst[j]<lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(lst)

if __name__ == "__main__":
    test = [90,56,90,24,56,23,8,5,0,123,7]

    dbubble(test)