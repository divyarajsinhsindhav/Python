#find gretest number betwwen three numbers
def gretest(i,j,k):
	if i>j or i>k:
		return f"{n1} is gretest"

		if j>k or j>i:
			return f"{n2} is gretest"

	return f"{n3} is gretest"

n1 = int(input("Enter number 1 :- "))
n2 = int(input("Enter number 2 :- "))
n3 = int(input("Enter number 3 :- "))
print(gretest(n1,n2,n3))				