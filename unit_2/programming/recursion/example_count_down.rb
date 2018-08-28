def count_down(arr, n)
	return arr if n < 0
	count_down(arr, n-1)
	arr.unshift n
	print arr
end

count_down([], 10)

