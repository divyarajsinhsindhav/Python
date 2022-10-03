#define function which will take list as argument and this function 
#will return reversed list 

#Example:-
#[1,2,3,4,5,6,7,8,9] ---------> [9,8,7,6,5,4,3,2,1]
#["bike","car"] ---------> ["car","bike"]
#you can use reverse method or string slicing [::-1]
#also try this with pop and append method

#
n = [1,2,3,4,5,6,7,8,9]

def rev(i):
	i.reverse()
	return i

print(rev(n))	

#
a = ["A","B","C"]

def rev(i):
	j = i[::-1]
	return j
print(rev(a))	
