require './methods.rb'

bplay_again = true

while bplay_again == true
	printIntro
	playGame
	bplay_again = ask_to_play_again
end