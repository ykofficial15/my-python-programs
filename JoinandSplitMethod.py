#SPLIT METHOS
user_info='yogesh 15'.split()
print(user_info)

numbers='1,2,3,4,5,6,7,9'.split(',')
print(numbers)

name,age=input("enter your name and age with comma separated").split(",")
print(name)
print(age)

#JOIN METHOD
user=['yogesh','15']
','.join(user)
print(user)