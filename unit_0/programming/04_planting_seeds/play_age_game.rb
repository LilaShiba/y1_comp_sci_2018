# Load methods from age game
require "./age_game.rb"

bask_to_play_again = true
#While loop to play game again
while bask_to_play_again == true
	intro
	ask_name
	ask_age
	age_res
	bask_to_play_again = ask_to_play_again
#End Game
end