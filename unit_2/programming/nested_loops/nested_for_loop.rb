def most_frequent_item_count(collection)
    #Hold value of the most counted int
    most_counter = 0

    #Outer Loop triggers inner loop per letter amount times in collection 
    for letter in collection do
        counter = 0
        #Inner loop will count x collection*collection times
        for letter_compare in collection do 
            if letter == letter_compare
                counter = counter + 1
            end
            #transfer counter to most counted
        if counter > most_counter
            most_counter = counter

        end
        puts letter
        end
    end
    puts most_counter
end

meow = [1,2,1]
most_frequent_item_count(meow)