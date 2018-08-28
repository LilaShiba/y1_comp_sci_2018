def largest(collection)
	largest_number = 0

	for number in collection do 
		big_number_store = 0
		for number_check in collection do
			if number_check > number
				big_number_store = number_check
			end
			if big_number_store > largest_number
				largest_number = big_number_store
				break
			end
		end
		puts largest_number
	end
end

big_list = [100, 200, 300, 400, 500, 1000000, 100]

largest(big_list)