def oddSum(n)
    if n <= 0
        return -1
    else
        return n*n
    end
end


def odd(n)
    if n <= 0
        return -1
    else
        # What the IB wanted
        a = (0...n).map { |x| x * 2 + 1 }
        puts a
        # Compare to our method
       return a.inject{|sum,x| sum + x }
    end
end