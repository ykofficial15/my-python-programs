def greater(a,b):
    if a>b:
        return a
    else:
        return b


num1=input("enter first number:")
num2=input("enter second number:")
bigger=greater(num1,num2)
print(f"{bigger}is greater")