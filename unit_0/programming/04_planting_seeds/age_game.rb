# init age_array
@age_array = []

def intro
	puts "welcome to my game!\nHope you like it!"
end 

def ask_name
	puts "What's your name?"
	name = gets.chomp
	puts " welcome #{name}\n That's a fun name"
	#TODO: if/else based on name
end

def ask_age
	puts 'what is your age '
	@age = gets.chomp.to_i
	#push age to array
	@age_array.push(@age)
	#add a test to see if scope is right
	puts "#{@age_array} it worked!"
end

def age_res
	if
		puts "wow, #{@age} is a baby"
	elsif @age <= 18
		puts "wow, #{@age} is still a baby"
	elsif @age <= 25
		puts "wow, #{@age} is when you should get a job!"
	else @age > 25
		puts "wow, #{@age} means you are old"
	end
end

def ask_to_play_again
	puts "would you like to play again? (y/n)\n"
	response = gets.chomp
	return response[0] == 'y' || response[0] == 'Y'

end