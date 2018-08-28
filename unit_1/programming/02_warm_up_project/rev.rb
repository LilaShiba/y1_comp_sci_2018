def solution(str)
  s_str = str.split('')
  neww=[]
  for x in s_str do
    neww << s_str.pop
   end
   return neww.join()
end

def alt_reverse(string)
  word = ""
  chars = string.each_char.to_a
  chars.size.times{word << chars.pop}
  word
end

def rev(str)
  word=""
  str_split = str.split('')
  while str_split.length >= 1 do
    word << str_split.pop
  end
  return word
end

meow = 'meow'
puts rev(meow)