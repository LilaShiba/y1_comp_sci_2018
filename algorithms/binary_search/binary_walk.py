# binary search
# Takes in an array, and a number to look for
def b_search(arr, find):
	# find middle of array
	mid = arr[len(arr)//2]
	# debug make sure it is the middle of an array
	print('the new middle is %d'%(mid))

	#Todos


	# what if the search number isn't in the array?
	# what if the array is empty?
	if len(arr) == 0 or (len(arr)==1 and arr[0]!= find):
		return False
	
	# what if the number is found?
	if find == mid: return True
	# condtional for lower half & upper half
	# recursion, pass in new arr, same find
	if find > mid: return b_search(arr[len(arr)//2+1:], find)
	# the colon denotes which half of the array to focus on 
	# // to return int rather than a float
	if find < mid: return b_search(arr[:len(arr)//2], find)
	


arr = [1,2,3,4,5,6,7,8,9,10]
print(b_search(arr,7))