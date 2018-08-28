def sum(arr)
  if arr.empty?
    return 0
  else
    number = arr.pop
    puts number + sum(arr)
  	return number + sum(arr)
  	end
end

sum([2,3,4]) # returns 7
