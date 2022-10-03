#Find factorial number using Python
#Logic :n! = n*(n-1)*(n-2)*_ _ _ _*1
def factor(i):
	if i == 1:
		return i
	return i*factor(i-1)

n = int(input("Enter any number :- "))

if n<0:
	print("Factorial of nagative numbers isn't possible")
elif n==0:
	print("Factorial of 0 is 1")
else:
	print(factor(n))		
			