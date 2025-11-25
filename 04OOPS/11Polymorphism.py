#Polymorphism means many forms

# we create multiple functions with the same name but they have diff forms

#Operator overloading- (+) operator do same thing add and concat 
print(2+3, "A"+"B")

# Two types of Polymorphism:
# 1. Function overriding( inheritance involve)- same fun name in both parent and child class 
# 2. Duck Typing

class Employee:
    def des(self):
        print("Employee")

class Teacher(Employee):
    def des(self):
        print("Teacher")

t1=Teacher()
t1.des() # Teacher

# 🔥 Duck Typing----------------------------------

# In Python, we don’t care about the class of an object…
# We only care about what the object can do.

# 👉 If an object walks like a duck and quacks like a duck,
# then Python treats it as a duck — even if its class name is not “Duck”.

# ⭐ What it REALLY means?

# If two different classes have functions with the same name and same purpose,
# Python allows you to use them interchangeably.

# Example:

# Two classes: Dog and Cat
# Both have a function called speak().

class Dog:
    def speak(self):
        print("Bark!")

class Cat:
    def speak(self):
        print("Meow!")


# Now a function that expects something that can “speak”:

def animal_sound(animal):
    animal.speak()   # Does not check if it is Dog or Cat


# Call it:

animal_sound(Dog())   # Bark!
animal_sound(Cat())   # Meow!


# ✔ Python doesn't check the type
# ❌ It doesn't ask: “Is this a Dog or a Cat?”
# ✔ It only checks: “Does this object have a speak() method?”

# 🧠 Why is it called Duck Typing?

# Because of the saying:

# “If it walks like a duck,
# and quacks like a duck,
# it is treated like a duck.”

# Meaning:
# If an object behaves like you expect, Python uses it — no need for strict types.