def total(a,b):
    return a+b

print(total(3,4))

def all_total(*args):
    total=0
    for num in args:
        total+=num
    return total

print(all_total(1,2,3,4,5,6,7,8,9))

