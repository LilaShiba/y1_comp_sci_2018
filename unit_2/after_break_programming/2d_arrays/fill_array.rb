odds = [1,3,5,7]
evens = [2,4,6,8]
result = [ ]

result.map { |x, y|  }



# Nested loop
puts 'Nested Loop Out Put: '
for x in odds do 
	for y in evens do
		result << [x, y]
	end
end

puts result.inspect
