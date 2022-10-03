#Output : odd or even

n = int(input("Enter any number :- "))

def odd_even(a):
	if a%2==0:
		return "even"
	else:
		return "odd"	
print(odd_even(n))	
