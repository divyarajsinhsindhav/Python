#Addition of user input number using for loop
n = int(input("Enter any number :- "))

total = 0
for i in range(1 , n + 1):
	total = total + i
print(total)