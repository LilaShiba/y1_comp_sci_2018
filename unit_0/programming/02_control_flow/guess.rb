# conditionals: https://launchschool.com/books/ruby/read/flow_control
# iterators: https://launchschool.com/books/ruby/read/loops_iterators
count = 1
puts "Welcome to the Number Guessing Game!"
puts "Guess a number between 1 and 100."
guess = gets.chomp.to_i
the_right_answer = rand(100)

while the_right_answer != guess
   guess = gets.chomp.to_i
  if guess == the_right_answer
    puts "You win! You guessed the answer in " + count.to_s + " tries!"
  elsif guess > the_right_answer
    count = count + 1
    puts 'guess lower: '
  elsif guess < the_right_answer
    count = count + 1
    puts 'guess higher: '
  else
    puts 'that is not a number'
  end
end

