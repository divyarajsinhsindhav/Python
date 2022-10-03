#Take 10 integers from keybord using loop and print their average value on the screen
a = input("Enter 10 digit number :- ")

total = 0
i = 0
while i < len(a):
	total += int(a[i])
	i += 1
avg = total/10	
print(avg)	
	