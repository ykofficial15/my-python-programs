fruits=['grapes','apple','mango']
fruits.sort()
print(fruits)
#sorted function in list
print(sorted(fruits))
#sorted function in sets
fruits2={'apple','banana','kiwi'}
print(sorted(fruits2))

smartphones=[
    {'brand':'apple','price':'120000'},
    {'brand':'realme','price':'11000'},
    {'brand':'samsung','price':'99000'},
    {'brand':'vivo','price':'60000'}
]
print(sorted(smartphones,key=lambda d:d['price']))
