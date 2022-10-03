#create function
#odd or even function in list

#input =
#number_list = [1,2,3,4,5,6,7,8,9,10]
#output = [[1,3,5,7,9],[2,4,6,8,10]]

n = [1,2,3,4,5,6,7,8,9]

def odd_even(a):
	b = []
	c = []
	x = [b,c]
	for i in a:
		if i%2==0:
			b.append(i)
		else:
			c.append(i)
	return x		
			  
print(odd_even(n))  
