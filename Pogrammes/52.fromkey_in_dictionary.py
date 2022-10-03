
user_info = {
	"name":"Divyrajsinh",
	"age":18
}

#from key
user = dict.fromkeys(["name","age","address"],"unkown") #We can also use Tuple at the place of List
print(user)

#get method
user_get = user_info.get("names","key is not found")
print(user_get)

#clear method
user_info.clear()
print(user_info)

#copy method
information = {
	"name":"Python",
	"age":30
}

print(information)
info1 = information.copy()
print(f"This Dictionary is copy of information Dictionary :- {info1}")
