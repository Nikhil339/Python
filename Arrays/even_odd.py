from array import array as ary

def even_odd(arr):
    even_numbers = ary('i',[num for num in arr if num % 2 == 0])
    odd_numbers = ary('i',[num for num in arr if num % 2 != 0])

    print("Even Numbers:", even_numbers.tolist())
    print("Odd Numbers:", odd_numbers.tolist())

array_num = ary('i',[1,2,3,4,5,6,7,8,9])
even_odd(array_num)