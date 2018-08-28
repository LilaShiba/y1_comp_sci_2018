def split_sum(n)
    # turn data type into string
    # return array of characters for n
    # turn array from str to int
    # add together
    return n.to_s.chars.map(&:to_i).inject:+
    
end