matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[0])
print(matrix[1])
print(matrix[2])
print("\n")
for i in matrix:
    print(i)

for sublist in matrix:
    for i in sublist:
        print(i)
print("\n")
print(matrix[1][1])
print(matrix[2][0])
print(type(matrix))