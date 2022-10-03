#user input split function
#user input is name,last_name,mobile_number,age
name,last_name,mobile_number,age = input("Please enter your name,last_name,mobile_number & age:- ").split(",")
print(f"Your name is {name} \nYour surname is {last_name} \nYour mobile_number is {mobile_number} \nYpur age is {age}") 

#user input
#e.g:
#5 + 5 + 5
# /3
no1 = input("Please your number1:- ")
no2 = input("Please your number2:- ")
no3 = input("Please your number3:- ")
print(f"The answer is {(int(no1)+int(no2)+int(no3))/3}")
