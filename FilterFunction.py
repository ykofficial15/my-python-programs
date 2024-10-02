#filter function
def is_even(a):
    if a%2==0:
        return True
    else:
        return False

numbers=[3,4,2,1,5,6,9,8,10]
evens=tuple(filter(is_even,numbers))
print(evens)

#by lambda function
evens=tuple(filter(lambda a:a%2==0, numbers))

new_evens=[ i for i in numbers if i%2==0]
print(list(evens))
print(new_evens)

