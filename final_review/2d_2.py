from pandas import *

m = [[1,2,3], [4,5,6], [7,8,9,], [10,11,12,13]]
#print(DataFrame(m))

# Nested loops are used to access 2-dimensional array
# The first loop iterates through the row number,
# The second loop runs through the elements inside of a row.
find = 2
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == find:
            print('hiya')
            print(m[i][j])

#for row in m:
    #for elem in row:
    #    print(elem, end=" ")
    #print()
