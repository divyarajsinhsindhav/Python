#1.input : Ask user to full name
#1.Output : Output by using string formating
#           print user full name in upper case & lower case
#           print the lenght of full name
name , last_name = input("Enter your full name:- ").split(" ")
full_name = name + last_name
print(full_name)
print(f"Your name is:- {name} \nYour last_name is:- {last_name}")
print(full_name.upper())
print(full_name.lower())
print(len(full_name))

#2.input : take two comma saprated input from user
#          input user name and any character
#2.output : count the character that user inputed
name , character = input("Enter your name & any character from your name:- ").split(",")
print(f"Your name is:- {name} \nYour inputed character is:- {character}")
size = name.count(character)
print(f"Your inputed character size in your name is {size}")
