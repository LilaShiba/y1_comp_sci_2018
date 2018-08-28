#fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]

def fibo_add_next(n)
	#Improve this to create fibonacci from 2 values
	for x in n do 
		new_num = n[-2] + n[-1]
	end
	puts new_num
		#Improve this statement
	if n[-1] - n[-2] == n[-3]
		puts "this is a fibonacci array"
	else
		puts "this is just junk"
	end
end

#fibo(fibonacci)