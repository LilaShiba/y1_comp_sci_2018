def order_me(data)
	newdata = data.sort do |a,b| b <=> a end
	puts newdata
end




meow = [50, 75, 20, 8, 1, 100]

order_me(meow)


#http://www.evc-cit.info/cit020/beginning-programming/chp_07/custom_sort.html
#https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm
#https://www.geeksforgeeks.org/linked-list-vs-array/