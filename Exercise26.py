class Laptop:
    def __init__(self,brand,name,price):
        self.brand=brand
        self.name=name
        self.price=price

laptop1=Laptop('asus','vivobook',33500)
print(laptop1.name)
print(laptop1.brand)
print(laptop1.price)
