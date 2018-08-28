def most_frequent_item_count(collection)
    #Hold value of the most counted int
    most_counter = 0

    #iterate over the collection to get first value
    for letter in collection do
        counter = 0
        #compare iterators to count 
        for letter_compare in collection do 
            if letter == letter_compare
                counter = counter + 1
            end
            #transfer counter to most counted
        if counter > most_counter
            most_counter = counter

        end
        end
    end
    return most_counter
end

meow = [1,2,2,2,1,5,6,6,5,1,1,3,2]
most_frequent_item_count(meow)