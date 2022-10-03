#find prime nunmber using python

n = int(input("Enter any integer number :- "))

isprime = True
for i in range(2,n//2+1):
	if n%i == 0:
		isprime = False
		break

if isprime==True:
	print(f"{n} is prime number")
else:
	print(f"{n} is not a prime number")			

