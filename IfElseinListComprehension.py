#simple method
nums=[1,2,3,4,5,6,7,8,9]
new_list=[]
for i in nums:
    if i%2==0:
        new_list.append(i*2)
    else:
        new_list.append(-i)

print(new_list)

#list comprehension
new_list2=[i*2 if(i%2==0) else -i for i in nums]
print(new_list2)
