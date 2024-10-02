numbers=list(range(1,11))
print(numbers)
numbers.pop()
print(numbers)
poped_item=numbers.pop()
print(poped_item)
print(numbers.index(2))

def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
        
    return negative

print(negative_list(numbers))