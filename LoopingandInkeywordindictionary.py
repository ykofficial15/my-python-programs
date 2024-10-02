user_info={
    'name':'yogesh',
    'age':20,
    'fav_movies':['spiderman','avengers','pushpa'],
}

#values method
if 'name' in user_info: #if 20 in user_info: bhi likh sakte hai
    print("present")
else:
    print("not present")

#loop in dictionaries
for i in user_info:
    print(i)

user_info_values=user_info.values()
print(user_info_values)
print(type(user_info_values))

#keys method-->it returns only heading/keys
user_info_keys=user_info.keys()
print(user_info_keys)
print(type(user_info_keys))
#by looping
for i in user_info:
    print(user_info[i])

#item method-->it returns a list in tuple form
user_items=user_info.items()
print(user_items)
print(type(user_items))
#by looping
for key,value in user_info.items():
    print(f"key is {key} and value is {value}")

for i in user_info.items():
    print(i)
