def num_split(n)
    # turn into str    
    nums = n.to_s
    # convert into array
    nums_array = nums.split("")
    # convert array into int
    int_nums = nums_array.map(&:to_i)
    # add all together
    sum = 0
    for x in int_nums do
        sum = x + sum    
   end
   puts sum
end