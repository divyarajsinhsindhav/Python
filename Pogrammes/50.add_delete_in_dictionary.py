#How to add & delete data from ditionary

user_info = {
	"name":"Divyrajsinh",
	"last_name":"Sindhav",
	"Country":"India"
}
print(user_info)

#how to add
user_age = int(input("Enter your age :- "))
user_info["age"] = user_age
print(user_info)

#pop method #(how to delete)
user_info.pop("last_name")
print(user_info)

#popitem method
user_info_popitem = user_info.popitem()
print(user_info_popitem)
