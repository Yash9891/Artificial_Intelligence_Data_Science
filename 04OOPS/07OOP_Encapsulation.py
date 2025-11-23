"""
4 Pillars of OOP
1. Encapsulation- Wrapping data and functions into a single unit- Data hiding
2. Abstraction
3. Inheritance
4. Polymorphism
"""

# Ex- Encapsulation- Hide the data (Make it private)---------------

# Public - Accessible inside class and outside class
# Private- Accessible only inside the class - add (__ double undescore before attribute)
# Protected- Accessible inside tha class and its subclass- add (_ single undescore before attribute)

class BankAccount:
    def __init__(self, name,balance):
        self.name=name
        self.__balance=balance # can not be accessible outside class

    # getter and setter to access private attributes
    def set_newbalance(self, newBalance): #setter
        self.__balance=newBalance

    def get_Balance(self): #getter
        return self.__balance

acc1=BankAccount("Rahul", 100000)
# print(acc1.name, acc1.__balance)  # balance not accessible 
print(acc1.name, acc1.get_Balance())

#setter
# acc1.__balance=4545  # can not update the price
acc1.set_newbalance(200000) # need to use setter to update price
print(acc1.name, acc1.get_Balance())

#Another way to access private attribute- So not true private attrivate just a layer
print(acc1._BankAccount__balance)

