
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
   print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
   print('-+-+-')
   print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
   print('-+-+-')
   print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'

for i in range(9):
	printBoard(theBoard)
	print('Turn for: ' +turn+ ' . Which Space?')
	move = input()
	theBoard[move] = turn
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
printBoard(theBoard)


# The printBoard() function can handle any tic-tac-toe data structure you pass it
# For example, the printBoard() function expects the tic-tac-toe data structure to 
# be a dictionary with keys for all nine slots. If the dictionary you passed was missing, 
# say, the 'mid-L' key, your program would no longer work.