#random = [18, 15, 13]

def max(collection)
	max_number = 0
	for number in collection do 
		for number_compare in collection do
			if number_compare > number and number_compare >= max_number
				max_number = number_compare
			end
		end
	end
	return max_number
end



#Out loop 13
#In loop 15
#max_number 18



