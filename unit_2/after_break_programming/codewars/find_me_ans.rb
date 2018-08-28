# init the method
# init my method with one arg
def find_me(arr)
  #int my outter iterator
  i = 0
  # init my first while loop
  while i < arr.length
    j = 0
    while j <= arr.length
      if j == arr.length
        return arr[i]
      elsif i == j || -(arr[i]) != arr[j]
        j += 1
      else
        break
      end
    end
    i += 1
  end
end 




 

def solve(arr)
 arr.each do |x|
    unless arr.include?(-x) 
      return x
    end
  end
end


def solve2(arr)
  arr.each {|x| return x if !arr.include? -x}
end


def solve3(arr)
 arr.each do |i|
 return i if !arr.include?(-i)
 end
end