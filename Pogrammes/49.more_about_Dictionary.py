#in keyword and iterations in dictionary
#check if key exit in dictionary
user_info = {"name":"Divyrajsinh","age":18}

if "name" in user_info: #check key
	print("present")
else:
	print("not present")
	
#check if value exist in dictionary --------> values method
if "Divyrajsinh" in user_info.values(): #check value
	print("present")
else:
	print("not present")	

#values method and key method
values_in_dictionary = user_info.values() #print all value of Dictionary
print(values_in_dictionary)

key_in_Dictionary = user_info.keys() #print all keys of ddictionary
print(key_in_Dictionary)

#loops in dictionaries
for i in user_info: #print key
	print(i)

for i in user_info.values(): #print values 
	print(i)

#item method
for key,value in user_info.items():
	print(f"The key is {key} and the value is {value} ")
