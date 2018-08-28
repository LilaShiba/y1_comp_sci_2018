# You have two stacks which you will use to create a thrid
# You will compare stack1[x] to stack2[y] and populate the thrid
# Stack with which ever iterators word length is even
# if both are even, then you would add just one case of the word

# Example
arr1= ['woof', 'mew', 'bork', 'craww', 'tricky']
arr2= ['borf', 'meow', 'growlll', 'chirps', 'tricky']
new_arr = []

# Example while loop
# index & value
i = 0
j = 0
while i < len(arr1):
    print(arr1[i])
    print(i)
    i = i + 1
    while j < len(arr2):
        print(arr2[j])
        j = j + 1
