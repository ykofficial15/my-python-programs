class Laptop:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.name=model_name
        self.price=price
        self.laptop_name=brand+' '+model_name

    def apply_discount(self,num):
        off_price= (num/100)*self.price
        return self.price - off_price

laptop1=Laptop('hp','pavillion',60000)
laptop2=Laptop('asus','vivobook',33500)
print(laptop2.apply_discount(5))
