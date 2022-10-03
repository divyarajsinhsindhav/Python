n = int(input("Enter numbers of rows :- ")) #n=5 

k = 0 

for i in range(1 , n+1): #i=1/
	for j in range(1 , (n-i)+1): #(n-i)+1 = 5 that's mean 4 space print 
		print(end=" ")

	while k!=(2*i-1): #k!=(2*i-1) = k!=1
		print("*",end="")
		k += 1

	k = 0
	print("\r")

#3210*0123
#210***012
#10*****01
#0*******0
#*********