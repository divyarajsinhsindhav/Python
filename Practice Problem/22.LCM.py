#Find LCM of any number using Python
#LCM = Product of greatest power of each priime factor

def LCM(x,y): #define function 'LCM'
	if x>y: #check greter number
		greatest = x #return 'LCM'
	greatest = y

	while True: #infinite loop
		if greatest%x == 0 and greatest%y == 0: #if greatest%x == 0 and greatest%y == 0
			LCM=greatest #than LCM=gretest
			break #Infinite loop is break

		greatest +=1 #incrimate in gratest

	return LCM

n1 = int(input("Enter number 1 :- "))
n2 = int(input("Enter number 2 :- "))

print(f"LCM of {n1} & {n2} is :- ",LCM(n1,n2))		
	