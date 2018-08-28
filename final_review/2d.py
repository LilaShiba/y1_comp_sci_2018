m = [[1,2,3], [4,5,6]]

find = 5
new_array = [];
# return all odd values into a new array
# rows
for o in range(len(m)):
    # o = the first array [[1,2,3], [4,5,6]]
    # o = [1,2,3]
    for i in range(len(m[o])):
        # if you are odd
        if m[o][i] % 2 == 1:
            # join the island of misfit toys
            new_array.append(m[o][i])
    print(new_array)
