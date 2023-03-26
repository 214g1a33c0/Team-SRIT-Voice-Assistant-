import random
def coin():
	print("Welcome to the coin flipping game")
	choice=input("Enter your side (head or tails) ")
	num=random.randint(1,2)
	if num==1:
		result="heads"
	elif num==2:
		result="tails"
	if choice==result:
		print("Good job! you won the game.",result)
	else:
		print("ohh... you lost",result)
		print("Thanks for playing.")
def number():
	number = random.randint(1, 100)
	attempts = 0  # count no of attempts to guess the number
	guess = 0
	while guess != number:
		guess = eval(input('Guess a number: '))
		attempts += 1
		if guess == number:
			print( 'Correct! You used', attempts, 'attempts!')
			break
		elif guess < number:
			print ( 'Go higher!')
		else:
			print ('Go lower!')
def dice():
	player1_score = 0
	player2_score = 0
	for i in range(10):
		player1_value = random.randint(1, 6)
		player2_value = random.randint(1, 6)
		print("Player 1 rolled: ", player1_value)
		print("Player 2 rolled: ", player2_value)
		if player1_value > player2_value:
			print("player 1 wins.")
			player1_score = player1_score + 1 
		elif player2_value > player1_value:
			print("player 2 wins")
			player2_score = player2_score + 1
		else:
			print("It's a draw")

	input("Press enter to continue.") 
	print("### Game Over ###")
	print("Player 1 score:", player1_score)
	print("Player 2 score:", player2_score)



















		
