num=input("enter more than one digit number")

total=0
i=0
while i<len(num):
    total+=int(num[i])
    i+=1
print(total)