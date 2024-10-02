#normal function
def is_even(a):
    if a%2==0:
        return True
    else:
        return False
print(is_even(5))
#lambda expression starts
#1
ans=lambda a: a%2==0
print(ans(3))
#2
last=lambda s:s[-1]
print(last('yogesh'))
#lambda with if else statement
#normal function
def fun(s):
    if len(s)>5:
        return True
    else:
        return False

print(fun('yogesh'))
#lambda expression
fun2=lambda s:True is len(s) > 5 
print(fun2('abs'))


