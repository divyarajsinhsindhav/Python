#    *
#   **
#  ***
# ****
#*****

n = 5
k = 2*n - 2

for i in range(0,n):
	for j in range(0,k):
		print(end=" ")
	for j in range(0,i+1):	
		print("*",end=" ")
	k = k-2
	print("\r")

