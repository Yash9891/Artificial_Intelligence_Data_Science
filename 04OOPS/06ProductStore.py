class Product:
    count=0
    def __init__(self, name,price):
        self.name=name
        self.price=price
        Product.count+=1

    def get_info(self):
        print(f" The price of {self.name} is {self.price}")
    
    @classmethod
    def get_count(cls):
        print(f" Total products in store = {cls.count}")

    @staticmethod
    def discount(price, discount):
        print(f" Discounted price = {price -(price*discount/100)}")


p1=Product("Phone", 1000)
p2=Product("Laptop", 10000)
p3=Product("Shirt", 6000)
p3.price=9000

p3.get_info()
Product.get_count() #Total products
p1.discount(p1.price, 20)