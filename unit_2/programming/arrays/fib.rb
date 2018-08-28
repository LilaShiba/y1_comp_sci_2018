def fibo(n)
	return n if n == 0 || n == 1
	
	x = 0
	y = 1

 
 	(1..n).each do
		z = (x + y)
		x = y
		y = z
	end
	puts y
end
fibo(4)