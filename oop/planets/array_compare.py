# method that compares two arrays
# and prints out what they have in common
def compare_array(arr1, arr2):
	compare = [thing for thing in arr1 if thing in arr2]
	print(compare)


# For string datatype
arr_dog = ['woof', 'bork', 'meow']
arr_cat = ['mew', 'borf', 'bork']

compare_array(arr_dog, arr_cat)

# for int datatype
nums = [1,2,3,4,5]
nums2 = [1,2,5,6,7]

compare_array(nums, nums2)
