def fun(x,n)
	if n <= 0
		return 1
	else
		puts x * fun(x, n-1)
	end
end

puts fun(2,3)