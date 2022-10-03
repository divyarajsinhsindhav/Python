#find odd or even number using range in python
no1 = int(input("Enter range number 1 :- "))
no2 = int(input("Enter range number 2 :- "))

for i in range(no1 , no2 + 1):
	if i % 2 == 0:
		print(f"{i} is even")
		continue
		i = i + 1

	else:
		print(f"{i} is odd")
