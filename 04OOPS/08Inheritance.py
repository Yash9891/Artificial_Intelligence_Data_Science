"""
Inheritance: Inheritance means one class (child class-derived class) can access
the properties and methods of another class (parent class-base class)
"""

class Employee:
    start_time="10am"
    end_time="6Pm"

    def change_time(self, new_endtime):
        self.end_time=new_endtime

class Teacher(Employee):
    def __init__(self, subject):
        self.subject=subject

class AdminStaff(Employee):
    def __init__(self, role):
        self.role=role

t1=Teacher("Math")
t1.change_time("5pm")
staff1=AdminStaff("Manager")
staff1.change_time("10pm")

print(t1.subject, t1.start_time, t1.end_time)
print(staff1.role, staff1.start_time, staff1.end_time)