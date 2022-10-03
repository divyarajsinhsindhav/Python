#						1
#					1		1
#				1		2		1
#			1		3		3		1
#		1		4		6		4		1
#	1		5		10		10		5		1
n = int(input("Enter Rows :- "))
coef = 1

for i in range(1,n+1):
	for k in range(1,n-i+1):
		print(" ",end="")

	for j in range(1,i):
		if j==0 or i==0:
			coef=1
		else:
			coef=coef*(i-j)//j
		print(coef,end=" ")
	print()		
