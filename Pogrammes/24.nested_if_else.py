#Nested if-else
#Use if-else in if-else
winning_number = 4

user = int(input("Enter number between 1 to 10:- "))

if user == winning_number:
	print("You win the Lucky draw")

else:
	if user > winning_number:
		print("Your input number is too high")
	else:
		print("You input number is too low")	
