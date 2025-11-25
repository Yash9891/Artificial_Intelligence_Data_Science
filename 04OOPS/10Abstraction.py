"""1. What is Abstraction?

Abstraction means hiding the internal implementation and showing only the essential features.

It tells what to do, not how to do it.

2. How Abstraction Works in Python

Python provides abstraction through abstract classes.

Abstract classes act as a blueprint for other classes.

They are created using the abc (Abstract Base Class) module.
Why is this useful?

Abstraction lets you:

Create a common structure (make_sound() must exist).

Hide the implementation details from the user of the class.

Ensure that all animals follow the same rule.
"""
from abc import ABC, abstractmethod

class Animal(ABC):  # we are hinding implementation details

    @abstractmethod  # there is no implementation : they got implement only in child class
    def make_sound(): # here we do not want to implement this function
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar")
class Cow(Animal):
    def make_sound(self):
        print("Moo!")

lio=Lion()
lio.make_sound()

cow=Cow()
cow.make_sound()