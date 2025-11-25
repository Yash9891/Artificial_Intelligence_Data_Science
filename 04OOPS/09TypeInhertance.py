"""
Types:
1. Single Level inheritance
2. Multi level  inheritance
3. Multiple Inheritance
"""

#Multilevel inheritance-----------------------------
# class Employee:
#     start="10am"
#     end="6pm"

# class AdminStaf(Employee):
#     def __init__(self, role):
#         self.role=role

# class Account(AdminStaf):
#     def __init__(self, salary, role):
#         super().__init__(role) # super keword is use to call the parent class constructor
#         self.salary=salary

# acc1=Account(2500, "Manager")
# print(acc1.role, acc1.salary, acc1.start)


#Multiple inheritance-----------------------------
class Teacher:
    def __init__(self, salary):
        self.salary=salary

class Student:
    def __init__(self, gpa):
        self.gpa=gpa

class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary) # Call parent constructor
        Student.__init__(self, gpa)
        self.name=name
tat=TA(1500, 9.3,"Yash")
print(tat.name, tat.salary, tat.gpa)
