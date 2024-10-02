#tuples with bracket parameters
mixed=(1,2,3,4.0)
print(type(mixed))
for i in mixed:
    print(i)

#tuple without parameters
guitars='yamaha','baton rouge','talor'
print(type(guitars))
print(guitars)

#tuple unpacking
guitarist='yogesh','kumawat','sardarpur'
guitarist1,guitarist2,guitarist3=(guitarist)
print(guitarist)

#list inside tuples
favourites=('southern magolia',['tokyo ghoul theme','landscape'])
favourites[1].pop()
favourites[1].append("we did it")
print(favourites)

print(max(mixed))
print(min(mixed))
print(sum(mixed))