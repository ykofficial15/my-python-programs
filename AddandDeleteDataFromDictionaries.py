user_info={
    'name':'yogesh',
    'age':20,
    'fav_movies':['pushpa','spiderman','avengers']
}
print("before updation\n")
print(user_info)
user_info['fav_songs']=['thunder','yummy']
print("after updation")
print(user_info)

#pop method-->it is used to delete a key
popped_item=user_info.pop('fav_movies')
print(f"popped item is {popped_item}")
print(user_info)
print(type(popped_item))
