#create a function that take list of word as argument and return list with reverse
#of every element in that list

#Example:
#["Python","Java","C++"] ---------> ["nohtyP","avaJ","++C"]

l = ["python","java","C++"]

def rev(x):
	a = []
	for i in x:
		a.append(i[::-1])
	return a 

print(rev(l))		