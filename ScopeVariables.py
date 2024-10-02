x=5           #global variable
def func():
    global x
    x=7
    return x  #local variable

print(x) #before function call
print(func())
print(x)  #after fuction call


      