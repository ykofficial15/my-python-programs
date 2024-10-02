#iterator vs iterable
#iterable
numbers=[1,2,3,4]
for i in numbers:
    print(i)

print('\n')
#-------------------------------------------
number_iter=iter(numbers)
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))

#iterator
squares=map(lambda a:a**2,numbers)
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))