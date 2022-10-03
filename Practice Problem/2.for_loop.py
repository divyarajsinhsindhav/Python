#ask user for input more than one digit number ------------>1213
#calculate sum of digit ------->1+2+1+3
n = input("Enter any number of more than one digit :- ")

total = 0
for i in range(int(n[0]) , len(n)):
	total += int(n[i])
print(f"Sum of your input :- {total}")	