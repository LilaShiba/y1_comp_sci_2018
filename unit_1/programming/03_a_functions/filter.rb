#http://queirozf.com/entries/ruby-map-each-collect-inject-reject-select-quick-reference
a = [2,3,4,5,6]
f = a.select { |e| e%2==0 }
puts f