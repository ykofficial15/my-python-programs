def function(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count

mixed=[1,2,3,[1,2],[3,4],[11,12,3]]
print(function(mixed))
