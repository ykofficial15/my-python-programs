#enumerate function
#without enumerate function
names=['abc','basd','yogesh']
pos=0
for name in names:
    print(f"{pos}-->{name}")
    pos+=1

#with enumerate function
for pos,name in enumerate(names):
    print(f"{pos}-->{name}")


#2
def find_pos(l,target):
    for pos,name in enumerate(l):
        if name==target:
            return pos
    return -1

print(find_pos(names,'basd'))


