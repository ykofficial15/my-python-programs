class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    def full_name(self):
        return f"{self.first_name}{self.last_name}"


p1=Person('yogesh','kumawat',19)
print(p1.first_name)
print(p1.last_name)
print(p1.age)
print(p1.full_name())
