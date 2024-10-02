user={}
name=input("enter your name")
age=input("what is your age")
movie=input("enter your favourite movies")
song=input("enter your favourite song")

user['name']=name
user['age']=age
user['movie']=movie
user['song']=song
for key,value in user.items():
    print(f"{key}:{value} ")
#print(user)

