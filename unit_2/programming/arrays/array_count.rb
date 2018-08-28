def most_frequent_item_count(collection)
   most_counted = 0
  (collection.uniq).each do |num|
    if collection.count(num) > most_counted
      most_counted = collection.count(num)
    end
  end  
  return most_counted
end