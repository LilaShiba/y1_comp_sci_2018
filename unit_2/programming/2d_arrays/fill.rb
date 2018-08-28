x = ['A', 'B', 'C']
y = ['D', 'E', 'F']

puts x.map { |x|
  y.map { |y| [x, y] }
}.inspect