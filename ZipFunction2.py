
l=[(1,2),(3,4),(5,6),(7,8)]
#operator * with zip function
print(list(zip(*l)))
#unpacking
l1,l2=list(zip(*l))
print(list(l1))
print(list(l2))
  