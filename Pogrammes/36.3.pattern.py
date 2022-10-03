#Print star('*') pattern using end & for loop

#OUTPUT e.g. : #*
               #**
               #***
          	   #****
#total row in this pattern is 4 and column is  4        


#'nested_for' is use for make patterns  

n = 10

for i in range(0,n):
	for j in range(0,i+1):
		print("*",end="")
	print("\r")