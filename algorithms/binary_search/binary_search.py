# Walk through: https://www.youtube.com/watch?v=IcK2Qyk3cUs
# If using python 3, use // as / is true div and returns float
# Search input array 'arr' for specified value 'val'
def binary_search(arr,val):
	# if our input is empty or if there is a single element
	# that is not the value we are looking for
	# return false

	if len(arr) == 0 or (len(arr)==1 and arr[0]!= val):
		return False
	# hold the value of the middle of the array
	mid = arr[len(arr)//2]

	if val == mid: return True
	# if the value is less than the middle value, recursive implementation
	# for lower half of the array
	if val < mid:
		# print(arr[:len(arr)//2])
		return binary_search(arr[:len(arr)//2], val)
	# if the value is more than the middle value, recursive implementation
	# for upper half of the array
	if val > mid:
		# print(arr[len(arr)//2+1:])
		return binary_search(arr[len(arr)//2:], val)

	#a[len(a):] - This gets you the length of a to the end.
	#It selects a range.
	#If you reverse a[:len(a)] it will get you the beginning
	#to whatever is len(a).

# fill an array with a loop
b = 0
arr2 = []
count = 0
while b < 10000:
	b = b + 1
	arr2.append(b)
# print(arr2) to see all the numbers
# call function and print
print(binary_search(arr2, 725))
