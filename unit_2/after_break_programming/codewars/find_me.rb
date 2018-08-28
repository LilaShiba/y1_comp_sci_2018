# You will be given an array of integers whose elements have both a negative 
# and a positive value, except for one integer that is either only negative 
# or only positive. Your task will be to find that integer.

def find_me(arr)
	outter = 0
	while outter < arr.length
		inner = 0
		while inner < arr.length
			if inner == arr.length
				puts arr[inner]
				return arr[inner]
			elsif inner == outter || -(arr[outter]) != arr[inner]
				inner = inner + 1

			else
				break
			end
		end
		outter = outter + 1
	end
end


arr0 = [1]						#  1
arr1 = [1,-1,2,-2,3] 			#  3
arr2 = [-3,1,2,3,-1,-4,-2]		# -4
arr3 = [1,-1,2,-2,3,3]			#  3

puts find_me(arr1)
puts find_me(arr2)
puts find_me(arr3)