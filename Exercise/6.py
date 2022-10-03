#ask user for natural number (a)
#print total of 1 from a
a = int(input("Enter any natural number :- "))

total = 0
i = 1
while i <= a:
	total = total + i
	i = i + 1
print(f"Addtion of your input number from 1 is :- {total}")
