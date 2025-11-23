'''✅ OOP – Classes and Objects (Easy Explanation)

In real life, a student has properties like name, marks, college, etc.
If you want to store data of many students, you don’t repeat the same variables again and again.
Instead, you create a class → a blueprint.

📌 Class = Blueprint of object

A class defines:

Attributes (properties)

Methods (functions / behaviours)

📌 Object = Instance of Class

An object is created from a class.
Example: If Student is a class → stu1, stu2 are objects.'''


# Class is a blueprint of student information
class Student:
    # These are class attributes (common for all students)
    subject = "Python"
    college = "Candor"
    year = "2nd year"

    def fun():
        print("WE are doing fun")


# Creating objects (students)
stu1 = Student()
stu2 = Student()

# Accessing properties using objects
print(stu1.subject, stu1.college)   # Output: Python Candor
print(stu2.year, stu2.college)      # Output: 2nd year Candor

