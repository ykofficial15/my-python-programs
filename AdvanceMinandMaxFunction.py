def func(item):
    return len(item)
names=['yogesh','kumawat','sardarpur']
print(max(names,key=func))
print(min(names,key=func))

#anonmyousfunction
print(max(names,key = lambda item:len(item)))
 #some part is remaining lecture162
 