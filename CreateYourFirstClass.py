class Person:
    def __init__(self,first_name,last_name,age):
        print('init method constructor get called')
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

p1=Person('hello','hi',19)
p2=Person('Yogesh','kumawat',19)
print(p1.first_name)
print(p2.first_name)
print(p1.last_name)
print(p2.last_name)
print(p1.age)
print(p2.age)

