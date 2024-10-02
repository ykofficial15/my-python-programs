numbers1=[2,4,6,8,10]
numbers2=[1,2,3,4,5,6]
#all function
evens=[]
for num in numbers1:
    evens.append(num%2==0)

print(evens)
print(all(evens))

#list comprehension
print(all([num%2==0 for num in numbers1]))

#any function
print(any(numbers2))