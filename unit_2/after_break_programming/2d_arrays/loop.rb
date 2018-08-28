# How to iterate
# Find highest and lowest

	#init 2d
a = [[1, 2], [3, 4]]


a.each do |(x, y)|
  puts x + y
end

	# or

a.each do |sub|
  sub.each do |int|
    puts int
  end
end