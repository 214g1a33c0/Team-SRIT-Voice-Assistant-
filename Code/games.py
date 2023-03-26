import random
import time
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
def quiz():
	#Welcome the user
	print("Welcome to the Simple Quiz Game!")
	time.sleep(1)
	chances = 1
	print("You will have", chances, "chance to answer correctly. \nPlease put the alphabet of the answer\n")
	time.sleep(2)
	score = 0
	question_1 = print("1) Father of green revolution in the world \\?\n(a) MS.Swamynadhan\n(b) Swamy Vivekananda \n(c) Norman Borlug \n(d) Mahatma Gandhi \n\n ")
	answer_1 = "c"
	for i in range(chances):
		answer = input("Answer: ")
		if (answer.lower() == answer_1):
			print("Correct! Good Job.\n")
			score = score + 1
			break
		else:
			print("Incorrect!\n")
			time.sleep(0.5)
			print("The correct answer is", answer_1, "\n\n")
	time.sleep(2)
	question_2 = print("2) What is the capital of Andhrapraadesh?\n(a) amaravathi\n(b) tirupathi\n(c) hyderabad\n(d) vijawayavada\n\n ")
	answer_2 = "a"
	for i in range(chances):
		answer = input("Answer: ")
		if (answer.lower() == answer_2):
			print("Correct! Good Job.\n")
			score = score + 1
			break
		else:
			print("Incorrect!\n")
			time.sleep(0.5)
			print("The correct answer is", answer_2, "\n\n")
	time.sleep(2)
	question_3 = print("3) What is the largest city of India?\n(a) Mumbai\n(b) Chennai\n(c) Delhi\n(d) Anantapur\n(e) Goa\n(f) Banglore\n\n ")
	answer_3 = "c"
	for i in range(chances):
		answer = input("Answer: ")
		if (answer.lower() == answer_3):
			print("Correct! Good Job.\n")
			score = score + 1
			break
	else:
		print("Incorrect!\n")
		time.sleep(0.5)
		print("The correct answer is", answer_3, "\n\n")
	time.sleep(2)
	question_4 = print("4) Second largsest poulation country?\n(a) India\n(b) China\n(c) America\n(d) Singapore\n\n ")
	answer_4 = "a"
	for i in range(chances):
		answer = input("Answer: ")
		if (answer.lower() == answer_4):
			print("Correct! Good Job.\n")
			score = score + 1
			break
		else:
			print("Incorrect!\n")
			time.sleep(0.5)
			print("The correct answer is", answer_4, "\n\n")
	time.sleep(2)
	question_5 = print("5) What is India's national animal?\n(a) Beaver\n(b) Canadian Horse\n(c) Tiger\n(d) Goose\n\n ")
	answer_5 = "c"
	for i in range(chances):
		answer = input("Answer: ")
		if (answer.lower() == answer_5):
			print("Correct! Good Job.\n")
			score = score + 1
			break
		else:
			print("Incorrect!\n")
			time.sleep(0.5)
			print("The correct answer is", answer_5, "\n\n")
	time.sleep(1)
	while score >= 4:
		print("Well done! Your score was", score)
		break
	while score <= 3:
		print("Better luck next time! Your score was", score)
		break
	print("Thank you for playing the Simple Quiz Game!")
