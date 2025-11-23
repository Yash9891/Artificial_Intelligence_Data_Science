""" Instance - Use self - They can access the class and instance attributes
# Class- Use cls - They can only access class attributes- We also use decorator- @classmethod 
# Static methods- No compulsoty parameter - no use cls and self. They can not access class and instance attributes- @staticmethod
# The logic is related to class ex. fun to calculate price 
"""


class Laptop:
    storage_type="ssd" # class attribute

    def __init__(self, RAM, storage): #instance attributes
        self.RAM=RAM
        self.storage=storage

    def get_info(self): # Instance method----------------
        print(f" laptop has {self.RAM} & {self.storage} {self.storage_type}")
     
    @classmethod  # It makes the below method to class method by changing it's behaviour
    def get_storage_type(cls): # class method----------------------
        print(f" Class stoatge {cls.storage_type}")
    
    @staticmethod
    def calc_discount(price, discount):
        final_price=price-(discount*price/100)
        print(f"Discount price {final_price}")
    
l1=Laptop("16gb","512gb")
l2=Laptop("8gb","412gb")

l1.get_info()

#class method calling
l2.get_storage_type()
Laptop.get_storage_type()

l1.calc_discount(40_000, 10)

