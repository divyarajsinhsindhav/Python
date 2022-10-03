#define a function which will take list containing numbers as input
#and return list containing cube of evry elements

#Example:
#numbers = [1,2,3,4,5]
#square_list(numbers) ---------> return -------------> [1,8,27,64,125]

n = int(input("Enter range of list :- "))

numbers = list(range(1,n+1))
print(numbers)

def cube(x):
	numbers = []
	for i in x:
		numbers.append(i**3)
	return numbers
print(cube(numbers))		
	