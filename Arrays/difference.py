from array import array as ary

def cal_diff(arr):
    avg = sum(arr)/len(arr)
    print(f"Average: {avg}")

    differences = ary("f", [num - avg for num in arr])

    print("Differences betweeen each number and the average:")
    for i, diff in enumerate(differences):
        print(f"Element {i} ({arr[i]}): {diff}")

array_num = ary("i",[10,20,30,40,50])
cal_diff(array_num)