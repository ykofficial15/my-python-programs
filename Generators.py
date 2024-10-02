#generators are iterators
l=[1,2,3,4]#iterable
i=iter(l)
print(next(i))
print(next(i))
print(next(i))

for num in map(lambda a:a**2,l):#iterator
    print(num)




