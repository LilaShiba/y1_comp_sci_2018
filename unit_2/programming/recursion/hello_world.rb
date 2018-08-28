# Goal Output
# array = [1,2,3,4,5]
# 1 + 2 + 3 + 4 + 5
# 1 + 2 + 3 + 9
# 1 + 2 + 12
# 1 + 14
# 15
#
# array[-1] last value in index
#
# add index values [-1] & [-2] into a new var
# pop out last 2 index value
# push in new var
# repeat


def sum_arr(arr)
	if arr.count < 2
		return 0
	else
		new_num = arr[-1] + arr[-2]
		arr.pop(2)
		arr.push(new_num)
		sum_arr(arr)
  	end
  	# What do you notice happening here?
  	# return arr will return one value and exit
  	puts arr
 end	

fun_array = [1, 2, 3]
sum_arr(fun_array)



