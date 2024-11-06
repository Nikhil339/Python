class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show(self):
        print("Name:", self.name," Age:", self.age)
    
def eldest(per1, per2):
    if per1.age > per2.age:
        return per1
    elif per2.age>per1.age:
        return per2
    else:
        return None
    
person1 = Person("Shyam", 56, "Male")
person2 = Person("Prasad", 60, "Male")

person1.show()
person2.show()

elder = eldest(person1, person2)
if elder:
    print(f"{elder.name} is the eldest.")
else:
    print("Both are of same age.")