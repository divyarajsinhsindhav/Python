'''
try:
	open("This.text")
except Exception as e:
	pass
print("Hello")			
'''


'''try:
	file = open("This.text","r")
except EOFError as e:
	print('eof error')
except IOError as e:
	print('io error')
finally:
	print('finally')
'''

'''
try:
	print("I will try this code and will throw exception if there is any problem")
except Exception as e:	
	print("I will run only if try block fails")
else:
	print("I will run only if there is no exception.Use this to run code which should only execute if there is no exception")
finally:
	print("This will be run in everyh case")
'''			