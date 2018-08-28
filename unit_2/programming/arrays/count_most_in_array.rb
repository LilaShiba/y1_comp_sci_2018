def most_frequent_item_count(collection)
  arr = []
  if collection.empty?
    return 0
  else 
    collection.each do |element| 
      arr.push(collection.count(element)) 
    end
  end 
  arr_uniq = arr.uniq!
  arr_count_uniq = arr.max
  puts arr_count_uniq
end

meow = [1,2,2,2,1,5,6,6,5,1,1,3,2]

most_frequent_item_count(meow)

