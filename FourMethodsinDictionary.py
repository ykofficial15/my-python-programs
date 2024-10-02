#from keys
d=dict.fromkeys(['name','age','height',"abc"],'unknown')
print(d)
d=dict.fromkeys(('name','age','height',"abc"),'unknown')
print(d)

#get method
d={'name':'YOGESH','age':'unknown'}
print(d.get('name'))
print(d.get('names'))

if 'name' in d:
    print("present")
else:
    print("not present")
    
if d.get('name'):
    print("present")
else:
    print("not present")

#copy method
d1=d.copy()
print(d1)

#clear method
d1=d
print(d1.popitem())

print(d)
d.clear()
print(d)

