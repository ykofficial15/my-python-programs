#any and all function
def my_sum(*args):
    total=0
    for num in args:
        total+=num
    return total

print(my_sum(1,2,3,4))

