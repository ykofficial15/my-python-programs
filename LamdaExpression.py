#lamda expression is also known as anonmyous function
from ast import Lambda


def add(a,b):
    return a+b
#main sirf niche ka code hai uppar ka 12 bajaye
add2=lambda a,b:a+b
print(add2(2,3))

#lambda used in built in function like map and other iterators
multiply=lambda a,b:a*b
print(multiply(2,3))
