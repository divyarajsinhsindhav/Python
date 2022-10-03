#Holow square pattern using python

n = int(input("Enter side of square :- ")) 
for i in range(n): 
	for j in range(n): 
		if i==0 or i==n-1 or j==0 or j==n-1: 
			print("*",end=" ") 
		else:
			print(" ",end=" ")
	print()			
		

#012345678			
#* * * * *0			
#*0123456*1				
#*		 *2												
#*		 *3							
#* * * * *4																			
				