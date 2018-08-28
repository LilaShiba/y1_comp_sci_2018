Word_length = 4
@right = 'bork'
@right_array = ['b', 'o', 'r', 'k']
@not_used = []
@used = []
@count = 0



	
	# introduce the game
	def printIntro()
		puts "Welcome to Hangman!\n"
		puts "The idea is to guess my #{Word_length} letter word\n"
		puts "Hint: It's an Isogram, which means no letters repeat\n"
		return
	end

	
	def guess()
		puts "Guess?\n "
		@guess = gets.chomp.downcase.to_s
		return
	end
	
	def check
		if @right.include? @guess and @guess == @right.to_s 
			puts "Good Job. The word is #{@guess}"
			exit
		elsif (@right_array - @used).empty? == true
			puts "good job the word was #{@right}"
			exit
		elsif @right.include? @guess and @guess != @right.to_s
				puts "Good Job. The word contains #{@guess}"
				@used.push(@guess)
		else
				puts "not even close"
				@not_used.push(@guess)
		end
	end

	def ask_to_play_again
		puts "would you like to play again? (y/n)\n"
		response = gets.chomp
		return response[0] == 'y' || response[0] == 'Y'
	end

	def play_game
		while @count < 5 
			guess
			check
			puts 'you have ' +(5 - @count).to_s+ ' turns left'
			puts "letters not used are: #{@not_used}"
			puts "letters used are: #{@used} "
			@count +=1
		end
	end


