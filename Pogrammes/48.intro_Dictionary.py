#dictionary intro
#What are dictionaries?
#unordered collection of data in key : value pair

#Why we use Dictionary?
#Ans:--->Because of limitation of lists,lists are not enough to represent real time data

#Which Type of data a dictionary can store

#how to create dictionaries
user_details1 = {"name":"Divyrajsinh","age":18}
print(user_details1)

user_details2 = {
	"name":"Python",
	"age":30,
	"skill":"All Rounder"
}
print(user_details2)

#second method to create dictionary
user_details3 = dict(name="Divyrajsinh",age=21)
print(user_details3)

#how to access data from dictionary
#we can`t use indexing like List
print(user_details3["name"])

#how to add data to empty dictionary
user_info = {}
name = input("Enter your name :- ")
age = int(input("Enter your age :- "))

user_info["name"] = name
user_info["age"] = age

print(user_info)



