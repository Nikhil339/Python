# creating dictionary with integer keys
Dict = {1:"Python", 2:"For", 3:"Beginners"}
print(Dict)

# using items()
employee = {"Name":"John", "Age":29, "Salary":25000, "Company":"Google"}
for x, y in employee.items():
    print(x, y)

# dictionary with mixed keys
Dict = {"Name":"Python", 1:[1,2,3,4]}
print(Dict)

# empty dictionary
Dict = {}
print(Dict)

# dictionary with each item as a pair
Dict = dict({1:"Python", 2:"For", 3:"Beginners"})
print(Dict)

Dict = dict([(1,"Python"),(2,"CSE1001")])
print(Dict)

# nested dictonaries
Dict = {1:"Python", 2:"For", 3:{"A":"Learners", "B":"Let's", "C":"Learn"}}
print(Dict)

# adding elements
Dict = {}
print(Dict)

Dict[0] = "Python"
Dict[2] = "For"
Dict[3] = "Freshers"
print(Dict)

Dict["Value_Set"] = 2, 3, 4 # adding set of values to a single key
print(Dict)

Dict[2] = "Welcome" # updating existing key value
print(Dict)

Dict[5] = {"Nested":{"1":"Life", "2":"Earth"}} # adding nested key value to dictionary
print(Dict)

# accessing elements from a dictionary
Dict = {1:"Python", "name":"For", 3:"Learners"}
print(Dict["name"])
print(Dict[1])

print(Dict.get(3)) # using get() method

# accessing elements from a dictionary
Dict = {"Dict1":{1:"Python"},
        "Dict2":{"Name":"World"}}
print(Dict["Dict1"])
print(Dict["Dict1"][1])
print(Dict["Dict2"]["Name"])

# deleting a key value
Dict = {5:"Welcome", 6:"To", 7:"Python",
        "A":{1:"Python", 2:"For", 3:"Life"},
        "B":{1:"Live", 2:"Life"}}
print(Dict)
del Dict[6]
print(Dict)

del Dict["A"][2] # deleting a key from nested dictionary
print(Dict) 

# pop() method
Dict = {1:"Python", "Name":"For", 3:"Learners"}
pop_ele = Dict.pop(1)
print(Dict)
print(pop_ele)

# copy() and = 
original = {1:"Python", 2:"World"}
new1 = original.copy()
new2 = original # does shallow copy
print("new1:", new1)
print("new2:", new2)
print("orignal:", original)

# values() key() 
original = {1:"Python", 2:"World"}
print(original.values())
print(original.keys())

# len()
Dict ={"brand":"Ford", "model":"Mustang", "year":1964}
print(len(Dict))

# iterating dictionary
Employee = {"Name":"John", "Age":29, "Salary":25000, "Company":"Google"}
for x in Employee:
    print(x)
    print(Employee[x])

print(list(Employee))
print(sorted(Employee))

#creating dictionaries
print({x:x**2 for x in (2, 4, 6)})
print(dict(sape=4139, guido=4127, jack=4089))

# combining dictionaries
d1 = {"a1":1}
d2 = {"a":2,"b":2}
d1.update(d2)
print(d1)

# clear()
Dict = {1:"Python", "Name":"For", 3:"Learners"}
Dict.clear()
print(Dict)

