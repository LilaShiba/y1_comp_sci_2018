# Refactored
def hello_world(n)
	return n if n < 0
	puts n
	hello_world(n-1)
end

hello_world(10)

# how many times will this method iterate?
# Solve for count_d(8)
# What is the poin of this method?