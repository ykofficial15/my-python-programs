s={'a','b','c'}
if 'a' in s:
    print("present")
else:
    print("not present")
    
#set unordered collection of items
for items in s:
    print(s)

#set math
s1={1,2,3,4}
s2={3,4,5,6}

#union
union=s1|s2
print(union)
#intersection

intersection=s1&s2
print(intersection)