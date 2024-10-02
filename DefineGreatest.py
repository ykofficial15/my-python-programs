def greater(a,b,c):
    if a!=b and c:

            if a>b and a>c:
              return a
            elif b>c and b>a:
                return b
            elif c>a and c>b:
                return c
    else:
        return "oops! values are same"

num1=input("enter a first value:")
num2=input("enter second value")
num3=input("enter third value")
greatest=greater(num1,num2,num3)
print(f"{greatest}is greater")