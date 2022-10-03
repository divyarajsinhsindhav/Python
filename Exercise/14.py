#create function
#find how muvch number of list inside list

#Example
#input :
#List = [1,2,[4,5,6],[7,8,9],[1,4,7]]

#Output : 
#3

def number_of_list_in_list(x):
	count = 0
	for i in x:
		if type(i) == list:
			count += 1
	return count		

List = [1,2,[4,5,6],[7,8,9],[1,4,7]]
print(number_of_list_in_list(List))