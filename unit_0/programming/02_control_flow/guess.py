import random
# Defining variables
n = random.randint(1, 100)
count = 1
guess = int(input("Guess a number from 1 to 100: "))
# Loop to keep Guessing
while n != "guess":
	if guess < n:
		print("Think Higher Buddy ")
		guess = int(input())
		count = count + 1
	elif guess > n:
		print("Got to get down to get right ")
		guess = int(input("How low do you go? "))
		count = count + 1
	else:
		print("Hurray! You got it! The number was " +str(n))
		print("It took you  " +str(count)+ " times to guess the number")
		break