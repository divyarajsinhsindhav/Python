#input number
#check if the number iis positive or negative or zero and disply
#print message
#use nested if-else
user = int(input("Enter any positive or negative number:- "))

if user == 0:
	print ("Your input is Zero")
else:
	if user > 0:
		print("Your input is positive")
	if user < 0:
		print("Your input is negative")		