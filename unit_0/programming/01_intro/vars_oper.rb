# Data Types str, int, bool
# String interpolation 
# Input Output
# If/else

puts 'what is your name'
hello = gets.chomp
puts "Hello, #{hello}"

puts 'how old are you?'
age = gets.chomp
puts age + ' ,wow, that is old'

if age.to_i > 20
	puts 'yikes'
elsif age.to_i. > 30
	puts ' double yikes'
else
	puts 'oh'
end

a = 10
b = 20
c = 10.0

puts a + b
puts a / b
puts a / c
puts a % b 
puts a * b
puts a** 




x = 10
x += 5 # Assigns a value of 15 to variable x (the same as x = x + 5)

y = 20
y -= 10  # Assigns a value of 10 to variable y (the same as y = y - 10)

x = 10;
y = 5;

x /= y; # Assigns a value of 2 to variable x (the same as x = x / y)

# ==	Tests for equality. Returns true or false
# .eql?	Same as ==.
# !=	Tests for inequality. Returns true for inequality or false for equality
# <	Less than. Returns true if first operand is less than second operand. Otherwise returns false
# >	Greater than. Returns true if first operand is greater than second operand. Otherwise returns false.
# >=	Greater than or equal to. Returns true if first operand is greater than or equal to second operand. Otherwise returns false.
# <=	Less than or equal to. Returns true if first operand is less than or equal to second operand. Otherwise returns false.
# <=>	Combined comparison operator. Returns 0 if first operand equals second, 1 if first operand is greater than the second and -1 if first operand is less than the second.



# 0> 1 == 1
	#=> true

# 0> 1.eql? 2
	#=> false

# 0> 10 < 1
	#=> false
# 0> 10 <=> 10
	#=> 0

# 0> 10 <=> 9
	#=> 1

# 0> 10 <=> 11
	#=> -1