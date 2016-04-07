import random

def game():
	high_score = 100000

	random_number = random.randint(1,100)

	print random_number

	print "Guess a number I'm thinking of! It's between 1 and 100."

	number_of_guesses = 0

	#while player_guess != random_number:
	while True:

		try:
			player_guess = int(raw_input("What number do you think? "))
		except:
			print "You need to give us a number between 1 and 100. Try again: "
			continue
		
		number_of_guesses = number_of_guesses + 1

		if player_guess == random_number:
			print "Congratulations! You guessed the right number."
			print "It took you this many times to guess it: {}".format(number_of_guesses)
			if number_of_guesses < high_score:
				high_score = number_of_guesses
				print "You have the high score, which is", high_score
			else:
				print "The high score is", high_score
			restart_option()
			break

		else:
			if player_guess > 100 or player_guess < 1:
				print "The number you enter needs to be between 1 and 100!!"
			else:
				if player_guess < random_number:
					print "That guess is too low, try again?"
				else:
					print "That guess is too high, try again?"
		


def restart_option():
	play_again = raw_input("Would you like to restart? Yes or No?: ")
	if play_again == "Yes" or play_again == "y" or play_again == "yes" or play_again == "Y":
		game()
	else:
		print "Thanks for playing! Bye!"

print "Hello! Welcome to our game!"

player_name = raw_input("What's your name? ")

print "Hi {}! Nice to meet you!".format(player_name)

game()