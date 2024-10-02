#sadharan tarika
numbers=list(range(1,11))
nums=[]
for i in numbers:
    if i%2==0:
        nums.append(i)
print(nums)

#list comprehension
even_nums=[i for i in numbers if i%2==0]
print(even_nums)

even_nums2=[i for i in range(1,11) if i%2==0]
print(even_nums2)

odd_nums=[i for i in range(1,11) if i%2!=0]
print(odd_nums)