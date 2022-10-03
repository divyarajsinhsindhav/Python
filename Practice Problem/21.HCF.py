#find HCF of any number using python
#HCF = Product of smallest of each common prime factor
def HCF(x,y):
	if x>y:
		smaller = y
	smaller = x

	for i in range(1,smaller+1):
		if x%i == 0 and y%i == 0:
				HCF = i
	return HCF	

n1 = int(input("Enter number 1 :- "))
n2 = int(input("Enter number 2 :- "))

print(f"HCF of {n1} & {n2} is :- ",HCF(n1,n2))
