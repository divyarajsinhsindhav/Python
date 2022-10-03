#What is Scope?

a=10 #a is global variable

def function():
	global a #a=5 is now global variable
	a = 5 # a is local variable
	return f"local variable is {a}"
print(function())	
 
print(f"global variable is {a}")
