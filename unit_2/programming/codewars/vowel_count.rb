def getCount(inputStr)
  counter = 0
  inputStr.split("").each do |x|
    if ["a", "e", "i", "o", "u"].include?(x)
    counter += 1
    end
  end
  counter
end