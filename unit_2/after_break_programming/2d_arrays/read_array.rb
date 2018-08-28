# Adding
a = [[1, 2], [3, 4]]
a.each do |(x, y)|
  puts x + y
end

# Reading with interpolation
a = [[1, 2], [3, 4]]
a.each do |(x, y)|
  puts "x is #{x} and y is #{y}" 
end