require './main.rb'
@bPlayAgain = true

while @bPlayAgain == true
	printIntro
	play_game
	@bPlayAgain = ask_to_play_again
	if @bPlayAgain == true
		@count = 0
		@used = []
		@not_used = []
	else
		exit
	end
end

#abstraction
#encaspulation