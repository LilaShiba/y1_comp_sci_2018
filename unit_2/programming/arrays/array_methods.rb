# Use next, pop, push, empty? in pry
# don't use -1 use .last can't use -1 for index
# on IB
# Create method to reverse values in an array

#example
# arr_1 = [1, 2, 3, 4, 5]
# arr_2 = []
# arr_1 = [1, 2, 3, 4]
# arr_2 = [5]
# arr_1 = [1, 2, 3]
# arr_2 = [5, 4]
# arr_1 = [1, 2]
# arr_2 = [5, 4, 3]
# arr_1 = [1]
# arr_2 = [5, 4, 3, 2]
# arr_1 = []
# arr_2 = [5, 4, 3, 2, 1]


def rev(arr)
	arr2 = []
	until arr.empty?
		last_num = arr.pop
		arr2 << last_num
	end
	print arr2
end
fun_arr = [8,9,10,11,12]
rev(fun_arr)