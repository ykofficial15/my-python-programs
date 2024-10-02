#map function: ek hi baar loop chala sakte hai
numbers=[1,2,3,4]
def square(a):
    return a**2
squares=list(map(square,numbers))
print(squares)

#by lambda funcion
squares=list(map(lambda a:a**2,numbers))
print(squares)

#by list comprehension
squares_new=[i**2 for i in numbers]
print(squares_new)

new_list=[]
for num in numbers:
    new_list.append(square(num))
print(new_list)

