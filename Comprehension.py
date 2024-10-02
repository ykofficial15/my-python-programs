#SYNTAX 1
squares=[]
for i in range(1,11):
    squares.append(i**2)

print(squares)

#SYNTAX2
square2=[i**2 for i in range(1,11)]
print(square2)

negative=[]
for i in range(1,11):
    negative.append(-i)
print(negative)

negative2=[-i for i in range(1,11)]
print(negative2)

names=['yogesh','kumawat','sardarpur']
new_list=['y','k','s']
new_list=[]
for name in names:
    new_list.append(name[0])
print(new_list)

names2=[name[0] for name in names]
print(names2)
