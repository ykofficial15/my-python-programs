def greater(a,b):
    if a>b:
        return a
    return b

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else: 
        return c

def new_greatest(a,b,c):
    bigger=greater(a,b)
    return greater(bigger,c)

print(new_greatest(1000,200,30000))
