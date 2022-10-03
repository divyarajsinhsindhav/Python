#list in list
#[[odd],[even]]
#if user input is odd number is store in odd sublist
#else number is store in even sublist

def odd_even(x):
	odd=[]
	even=[]
	i=[odd,even]
	for j in x:
		if j%2==0:
			even.append(j)
		else:
			odd.append(j)
	return i			

List = []

while True:
	print("For exit pogramm enter 00")
	n = int(input("Enter any number :- "))
	List.append(n)
	print(odd_even(List))
	print("\n")

	if n==0:
		break


