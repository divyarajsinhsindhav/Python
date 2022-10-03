#define the function that takes a number(n)
#return a dictionary conttaining a square of number from 1 to n

#Example:
#Square_Finder(4)
#o/p:
#{1:1,2:4,3:9,4:16}

def square_finder(x):
	square = {}
	for i in range (1,x+1):
		square[i] = i**2
	return square	

print(square_finder(4))		