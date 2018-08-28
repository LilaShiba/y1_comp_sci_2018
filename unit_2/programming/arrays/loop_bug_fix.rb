random = [20, 19, 18, 20]
def most(collection)
	highest = 0
	for number in collection do 
		puts " outer loop is: #{number}" 
		for number_compare in collection do 
				puts number_compare
				if number_compare >= number
					highest = number_compare
				end
			end
		end
		puts highest
	end

most(random)