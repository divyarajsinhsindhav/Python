#'nested_for' is use for make patterns  

n = 10

for i in range(0,n):
	for j in range(0,i+1):
		print(j,end="")
	print("\r")
