#break & continue 
#nested if_else
#or operaters
#if user enter number out of limit print the massege
#system genrate randomly wining_number

import random

wining_number = random.randint(1,20)

while True:

	i = int(input("Guess any number between 1 to 20 :- "))

	if i == wining_number :
		print("You win the game.")
		break

	else:		
		
		if i > 20 or i < 1:
			print("You enter the number out of the limit")
		else:
			print("You guess the wrong number")	
			continue