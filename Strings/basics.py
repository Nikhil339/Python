# multi line strings
my_string = """Hello, Welcome to
the world of python"""
print(my_string)

# accessing string characters
str = "VITVELLORE"
print("str=",str)
print("str[0]=", str[0])
print("str[-1]=", str[-1])

print("str[1:5]=", str[1:5])
print("str[5:-2]=", str[5:-2])
print("str[3:]=", str[3:])

# slicing
String = 'ASTRING'

s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)

print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])

# + and *
str1 = "Hello"
str2 = "World!"

print("str1 + str2 =", str1 + str2)
print("str1*3 =", str1*3)

# iterating through a string
count = 0
for letter in "Hello World":
    if letter == "l":
        count += 1
print(count,"letters found")

# enumerate()
s1 = "geek"
obj1 = enumerate(s1)
print(type(obj1))
print(list(enumerate(s1)))
print(list(enumerate(s1,2)))

# find()
text= "This is a dummy string"
print(text.endswith('ing')) # may provide optional start and end indices
print(text.startswith('This')) # may provide start and end indices
print(text.find('is')) # returns start index of 'is' first occurrence
print(text.find('is', 4)) # starting at index 4, returns start index of 'is' first occurence
print(text.rfind('is')) # returns start index of 'is' last occurrence
print(text.index('is')) # like find but raises error when substring is not found
print(text.rindex('is')) # like find but raises error when substring is not found

# replace()
mystr = "this is a dummy string"
print(mystr.replace('dummy', 'great')) 

#separate a string
print(mystr.partition('is')) # from left to right
print(mystr.rpartition('is')) # from right to left
