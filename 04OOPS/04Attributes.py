# Class attributes belong to class
# INstance attributes belong to object

class Student:
    college_name="ABC college" # class attributes
    PI=3.14

    def __init__(self, name, gpa): # instance attributes
        self.name=name
        self.gpa=gpa
        self.PI=3.14

std1=Student("Rahji", 5.9)
print(std1.name, std1.college_name) # we cann acces class and instance attributes with obj
print(Student.college_name)

#If class and instance have same attribute then Instance attribute will be top priority

print(std1.PI) # Only instance attribute will be called first
