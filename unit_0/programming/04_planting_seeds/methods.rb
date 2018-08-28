#TODO: Init age_array

def printIntro
	puts "hello, and welcome to this awesome\nintro I made. Please tell me your name: "
	@name = gets.chomp
	puts "Oh wow, #{@name} is pretty strange sounding\nI guess that is alright"

end

def askQuestion
	puts "Please tell me how old you are: "
	@age = gets.chomp.to_i
	#TODO:push age to age_array 
end

def checkAge
	if @age <= 15
		puts "wow #{@age} is a baby"
	elsif @age < 18
		puts "Still can't vote at #{@age}\nSee you later!"
	else

		puts "Sorry to hear\n#{@age} is pretty old"
	end
end

def playGame
	askQuestion
	checkAge
end

def ask_to_play_again
	puts "would you like to play again? (y/n)\n"
	response = gets.chomp
	return response[0] == 'y' || response[0] == 'Y'

end




