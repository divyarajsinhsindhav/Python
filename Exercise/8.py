#Break & Continue
#While True

wining_number = 3

while True:

	a = int(input("Guess the number between 1 to 10 :- "))

	if a == wining_number:
		print("You win the game :)")
		break
	else:
		print("You loss the game :(")
		continue