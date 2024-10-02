s={ 1,2,3,2}

l=[1,2,3,4,5,4,3,2,1]
s2=list(set(l))
print(s2)

s.add(4)
s.add(7)
s.add(9)
s.remove(3)
print(s)

s.discard(4)
print(s)
s1=s.copy()
print(s1)
s.clear()
print(s)
