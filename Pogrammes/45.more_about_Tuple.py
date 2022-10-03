#looping in Tuple
name = ("Python","php","C++","Django","Laravel")
for i in name:
	print(i)

#Tuple with one element
#n = ("Divyrajsinh") #This is not one Element Tuple
n = ("Divyrajsinh",)
print(type(n))

#Tuple without ()
i = "Mongo DB","My SQL","SQL Lite"
print(i)

#Tuple Unpacking
name = ("Python","php","C++","Django","Laravel")
l1,l2,l3,l4,l5 = (name)
print(l1)

#list inside Tuple
x = ("Python","php","C++",["Django","Laravel"],["Mongo DB","My SQL","SQL Lite"])
print(x)

#Some function that you can use with Tuple
#min , max , sum 

number = (1,2,3,4,5,6,7,8,9)
print(min(number)) #find min number from Tuple
print(max(number)) #find max number from Tuple
print(sum(number)) #print sum of every number of Tuple




