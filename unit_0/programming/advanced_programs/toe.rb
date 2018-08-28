theBoard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def printBoard(board)
   puts " #{board[0]} | #{board[1]} | #{board[2]} "
   puts '-----------'
   puts " #{board[3]} | #{board[4]} | #{board[5]} "
   puts '-----------'
   puts " #{board[6]} | #{board[7]} | #{board[8]} "
end

turn = 'X'

for i in theBoard
	printBoard(theBoard)
	print('Turn for: ' +turn+ ' . Which Space?')
	move = gets.to_i
	theBoard[move] = turn
	if turn == 'X'
		turn = 'O'
	else
		turn = 'X'
	end
end
