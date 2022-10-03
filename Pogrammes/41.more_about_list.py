#how to print list by using range function 
number = list(range(1,11)) 
print(number)

#index method
i = [1,2,3,4,5,6,7,8,5,9]
print(i.index(5)) #print element '5' position in list
#print(i.index(5,5)) #print element second '5' position in list
#print(i.index(5,5,9)) #chack till 9th position in list & print elment '5' position

#pass list to a function 
def num(x): #addtion 5 in List`s every Elements
	number = []
	for i in x:
		number.append(i+5)
	return number

n = [1,2,3,4,5,6,7,8,9]			
print(num(n))