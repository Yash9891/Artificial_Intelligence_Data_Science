"""
✅ What is a Constructor (__init__())?

A constructor is a special function inside a class that runs automatically whenever you create a new object.

Think of it like:

When you make a new student object → the constructor fills the student’s details.

You do not need to call it manually.
When you create stu1 or stu2, Python calls the constructor by itself.

✅ Python automatically creates a constructor if we don't define one

If you don’t write your own __init__(), Python provides a default empty constructor.

✅ What is self?

self always refers to the current object.

Example:

When stu1 is created → self refers to stu1

When stu2 is created → self refers to stu2

Each object gets different values stored inside self.
"""

class Student:
    def __init__(self, name,cgpa):
        print("Constuctor was called")
        self.name=name
        self.cgpa=cgpa
        # self.name would be diff for each obj
    def get_cgpa(self):
        return self.cgpa


stu1=Student("Urvashi", 4.6)
stu2=Student("Raman",9.9)
print(stu2.name, stu2.cgpa)

print(stu2.get_cgpa())

