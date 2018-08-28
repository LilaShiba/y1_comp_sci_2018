# You have two stacks which you will use to create a thrid
# You will compare stack1[x] to stack2[y] and populate the thrid
# Stack with which ever iterators word length is even
# if both are even, then you would add just one case of the word

# Example
arr1= ['woof', 'mew', 'bork', 'craww', 'tricky']
arr2= ['borf', 'meow', 'growlll', 'chirps', 'tricky']

# correct output
new_arr=['woof', 'meow', 'bork', 'chirps', 'tricky', 'tricky']

#def new(arr1, arr2):
#    count = 0
#    while count < len(arr1):
#        print(arr1[count])
#        count = count + 1
#new(arr1,arr2)


def newer(arr1, arr2):
    new_arr2 = []
    for x in arr1:
        if len(x) % 2 == 0 and x not in new_arr2:
                new_arr2.append(x)
        for y in arr2:
            if len(y) % 2 == 0 and y not in new_arr2:
                    new_arr2.append(y)
    print(new_arr2)

newer(arr1, arr2)
