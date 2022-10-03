def greter(i,j):
	if i>j:
		return i
	return j
	
def new_greter(i,j,k):
	#bigger_number = greter(i,j)		
	#return greter(bigger_number,k)
	return greter(greter(i,j),k)

print(new_greter(12,13,14))

