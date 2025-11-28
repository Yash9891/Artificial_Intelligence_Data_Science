#1. Q1. Create a class with attributes account_number, owner_name,
#and balance

# class BankAccount:
#     def __init__(self, account_num, name, balance):
#         self.account_num = account_num
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print(f"{amount} Rs Credited. Total balance: {self.balance}")

#     def withdraw(self, amount):
#         self.balance = self.balance - amount
#         print(f"{amount} Rs Debited. Total balance: {self.balance}")

#     def checkBalance(self):
#         print(f"Total balance is {self.balance} Rs")


# yash = BankAccount(2345625245, "Yash", 500)
# yash.checkBalance()
# yash.deposit(200)
# yash.withdraw(100)


"""Q2. Create a class with the following attributes:
• title
• author
• list of reviews
And add methods to:
• add a new review
• count reviews
• display all reviews"""

# class Book:
#     def __init__(self, title, author, reviews=None):
#         self.title = title
#         self.author = author
#         self.reviews = reviews if reviews is not None else []

#     def add(self, review):
#         self.reviews.append(review)
#         print("Review added")

#     def count_review(self):
#         total = len(self.reviews)
#         print(f"Total reviews = {total}")

#     def display(self):
#         print(f"Book Name: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Reviews: {self.reviews}")


# darkhole = Book("Dark Hole", "Yash", ["This is a good book"])
# darkhole.count_review()
# darkhole.add("Not that good")
# darkhole.display()


"""
Concept: Encapsulation
Q3. Create a class with private attributes _name,_roll_no, and _marks.
Provide getter and setter methods with validation (e.g., marks cannot be
negative, roll number has to be between 1 &100&name cannot be empty)."""

# class Student:
#     def __init__(self, name, roll_no, marks):
#         self.__name = name        # private
#         self.__roll_no = roll_no  # private
#         self.__marks = marks      # private

#     # ---------- SETTERS WITH VALIDATION ----------
#     def set_name(self, name):
#         if name.strip() != "":
#             self.__name = name
#         else:
#             print("Error: Name cannot be empty!")

#     def set_roll_no(self, roll_no):
#         if 1 <= roll_no <= 100:
#             self.__roll_no = roll_no
#         else:
#             print("Error: Roll number must be between 1 and 100.")

#     def set_marks(self, marks):
#         if marks >= 0:
#             self.__marks = marks
#         else:
#             print("Error: Marks cannot be negative.")

#     # ---------- GETTERS ----------
#     def get_name(self):
#         return self.__name

#     def get_roll_no(self):
#         return self.__roll_no

#     def get_marks(self):
#         return self.__marks

#     # ---------- DISPLAY ----------
#     def display(self):
#         print(f"Name: {self.__name}, Roll No: {self.__roll_no}, Marks: {self.__marks}")

# yash = Student("Yash", 23, 90)
# yash.set_marks(99)
# yash.set_roll_no(34)
# yash.display()

"""
Concept: Function Overriding
Q4. Create a class Shape with a method area().
Create subclasses Circle , , and that override the area()
method."""

# class Shape:
#     def area(self):
#         print("Area not defined for generic shape")


# class Circle(Shape):
#     def area(self, r):
#         return 3.14 * r * r


# class Rectangle(Shape):
#     def area(self, l, b):
#         return l * b 


# class Triangle(Shape):
#     def area(self, b, h):
#         return 0.5 * b * h  

# c = Circle()
# print(c.area(5))       # Circle area

# r = Rectangle()
# print(r.area(4, 6))    # Rectangle area

# t = Triangle()
# print(t.area(3, 4))    # Triangle area


"""
Concept: Inheritance
Q5. Create a base class Vehicle with attributes like brand and model.
Create two subclasses Car and Bike that add extra attributes - seats (in Car)&
engine_cc (in Bike)."""

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# class Car(Vehicle):
#     def __init__(self, brand, model, seats):
#         super().__init__(brand, model)   # Call parent constructor
#         self.seats = seats

# class Bike(Vehicle):
#     def __init__(self, brand, model, engine_cc):
#         super().__init__(brand, model)   # Call parent constructor
#         self.engine_cc = engine_cc

# # Create objects
# car1 = Car("Toyota", "Fortuner", 7)
# bike1 = Bike("Honda", "CBR", "250cc")

# # Print details
# print(car1.brand, car1.model, car1.seats)
# print(bike1.brand, bike1.model, bike1.engine_cc)


"""
Concept: Abstraction
Q6. Create an abstract class with an abstract method
calculate_salary().
Create subclasses , , and that
implement the method differently.
"""
# from abc import ABC, abstractmethod

# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self, salary, tax):  # must include self and parameters
#         pass  # hides the implementation of calculation

# class Intern(Employee):
#     def calculate_salary(self, salary, tax):
#         self.salary = salary - tax
#         return self.salary

# class FullTime(Employee):
#     def calculate_salary(self, salary, tax):
#         self.salary = salary - tax
#         return self.salary

# yash = Intern()
# rahul = FullTime()

# print(yash.calculate_salary(5000, 200))
# print(rahul.calculate_salary(10000, 500))


# You cannot create an object of Employee.

# Subclasses must override calculate_salary().


"""
Concept: Constructor Overloading (with Default Parameters)
Q7. Create a class that allows the constructor to work with:
• name only
• name + age
• name + age + address
As direct constructor overloading (multiple constructors) are not allowed but
we have to use default parameters to simulate constructor overloading"""


# class Person:
#     def __init__(self, name, age=45, address="Delhi"):
#         self.name = name
#         self.age = age
#         self.address = address

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Address:", self.address)

# # 1️⃣ Only name
# p1 = Person("Yash")

# # 2️⃣ Name + age
# p2 = Person("Rahul", 22)

# # 3️⃣ Name + age + address
# p3 = Person("Madhuri", 21, "Pune")

# p1.display()
# print()
# p2.display()
# print()
# p3.display()


"""
Concept: Instance & Class Attributes
Q8. Create a class with:
• a class variable player_count
• instance variables name and level
Track how many players were created."""

# class Player:
#     # class variable
#     player_count = 0

#     def __init__(self, name, level):
#         self.name = name
#         self.level = level
#         Player.player_count += 1   # increase count when a player is created


# # creating objects
# yash = Player("Yash", 45)
# rahul = Player("Rahul", 25)
# paul = Player("Paul", 49)
# paul = Player("Paul", 49)

# print("Total players created:", Player.player_count)


"""
Concept: Multiple Inheritance
Q9. Create the following classes: Herbivore , Carnivore , with some
attributes & methods. Then create a class Bear that inherits from all the above
classes to showcase how multiple inheritance works."""

# Concept: Multiple Inheritance

# class Herbivore:
#     def __init__(self):
#         self.food_type = "Plants"

#     def eat_plants(self):
#         print("Eats plants")


# class Carnivore:
#     def __init__(self):
#         self.hunt_skill = "Strong Hunter"

#     def eat_meat(self):
#         print("Eats meat")


# # Bear inherits from BOTH Herbivore and Carnivore
# class Bear(Herbivore, Carnivore):
#     def __init__(self):
#         Herbivore.__init__(self)
#         Carnivore.__init__(self)
#         self.name = "Bear"

#     def show(self):
#         print("Name:", self.name)
#         print("Food Type:", self.food_type)
#         print("Skill:", self.hunt_skill)


# b = Bear()
# b.show()
# b.eat_plants()
# b.eat_meat()


"""
Q10. Mini Project – OOP Chat System
Letʼs create a Chat System using OOPs concepts. We have to create classes:
•
•
•
And we have to implement functions:
• sending messages
• viewing chat history
• user joining and leaving the chatroom
"""

