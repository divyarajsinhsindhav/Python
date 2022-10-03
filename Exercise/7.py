#ask user to input any number of more than one digit
#e.g : 1213
#calculate 1+2+1+3 and print
a = input("Input any number of more than one digit :- ")

total = 0
i = 0
while i < len(a):
	total += int(a[i])
	i += 1
print(f"Additon of your Input digit is :- {total}")