def evenMax (collection)
	max_even_number = 0
	max_prime_number = 0
	for number in collection do 
		for number_compare in collection do 
			if number_compare >= number and number_compare.even?
				if number_compare >= max_even_number
				max_even_number = number_compare
				end
			end


			if number_compare > number and number_compare.odd?
				max_prime_number = number_compare
			end
		end
	end
	puts "max even number is " + max_even_number.to_s 
	puts "max prime number is " + max_prime_number.to_s 
end


# call
t = [24, 10, 17, 11, 20, 12, 13, 14, 23]
evenMax(t)

# Load in PRY