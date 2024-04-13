def findsum(lst,num):
    if num == 0:
        return 0
    else:
        return lst[num-1]+findsum(lst,num-1)
    
mylist = []
num = int(input("Enter how many numbers: "))
for i in range(num):
    n = int(input("Enter Element "+str(i+1)+": "))
    mylist.append(n)

sum = findsum(mylist,len(mylist))
print("Sum of list itmes", mylist,"is:",sum)