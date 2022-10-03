#Order or collection of items of is list
#List is collection which is order and changeble.Allows dupllicate mambers
#We store anything in list Exaple numbers,string,floting number,int etc.

numbers = [1,2,3,4,5,6,7,8,9,0]
print(numbers)
numbers[1] = "Divyrajsinh" #Change in list at 1st position
print(numbers)

mixed = [1,2,"Divyrajsinh",0.1213,12.13] #String,flot,int etc. allowed in string
print(mixed)
print(mixed[2]) #print 2nd position 

n = [0,9,8,7,6,5,4,3,2,1]
print(n[0:4]) #print 0 to 3rd position list

i = [1,3,5,7,9,0,2,4,6,8]
i[1:] = "Divyrajsinh"
print(i)

j = [7,8,9,4,5,6,1,2,3]
j[1:] = ["Divyrajsinh","K","Sindhav"]
print(j)


