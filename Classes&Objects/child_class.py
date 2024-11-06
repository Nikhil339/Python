class Details:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_details(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")

class Student(Details):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_student(self):
        self.display_details()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")

class Staff(Details):
    def __init__(self, name, age, staff_id, position):
        super().__init__(name, age)
        self.staff_id = staff_id
        self.position = position
    
    def display_staff(self):
        self.display_details()
        print(f"Staff ID: {self.staff_id}")
        print(f"Position: {self.position}")

student = Student("Ram", 19, "CSE1001", "Computer Science")
student.display_student()
print()
staff = Staff("Kumar", 26, "CS456", "Professor")
staff.display_staff()
