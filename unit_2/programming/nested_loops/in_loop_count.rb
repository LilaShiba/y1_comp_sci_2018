meow = [1,2,3,4,5]

out_loop = 0
in_loop = 0

for x in meow
	out_loop = out_loop + 1
	puts x
	for y in meow
		in_loop = in_loop + 1
		puts y
	end
end

#puts "in loop final: " + in_loop.to_s
#puts "out loop final: " + out_loop.to_s
