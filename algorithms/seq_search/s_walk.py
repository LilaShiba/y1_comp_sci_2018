# Sequential Search  		
def s_search(arr, missing):
	# iterate through list
	for x in range(len(arr)):
		# compare index value to missing
		if arr[x] == missing:
			# return index
			print(x)


# fill an array with a loop
b = 0
arr2 = []
count = 0
while b < 10000:
	b = b + 1
	arr2.append(b)

s_search(arr2, 100)