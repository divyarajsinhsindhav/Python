#print dictionatry
#o/p :
#user = {
#	"name":"Divyrajsinh"
#	"age":18
#	"language":"Gujrati"
#}

#also print this,
#The key is name and the value is Divyrajsinh
#The key is age and the value is 18
#The key is key is language and the value is Gujrati

user = {}

name = input("Plese enter your name :-")
age = int(input("Plese enter your age :-"))
language = input("Plese enter your language :-")

user["name"] = name 
user["age"] = age
user["language"] = language 

print(user)

for i,j in user.items():
	print(f"The key is {i} and the value is {j}")
