# *args and **kwargs
# *vars and **kvars

def function_1(name,age,rollno):
	print("The name of the student is",name,"and age is",age,"& Roll No. is",rollno)
#function_1('Divyraj',17,24)	


def function_2(*args): #Type of *args is Tuple
	if (len(args) == 3):
		print('The name of the Pogrammer is',args[0],'And the pogramming language is',args[1],'& age is',args[2])
	else:
		print('The name of the Pogrammer is',args[0],'And the pogramming language is',args[1])
#lis = ('harry','python')
#function_2(*lis)
#function_2('Divyraj','Django',17)


def marks(**kwargs): #Type of **kwargs is Dictionary
	for key,value in kwargs.items():
		print(key,value)
marklist = {'Divyraj':100,'Tony':98,'Peter':95}
#marks(**marklist)

def master(normal,*args,**kwargs):
	print(normal)
	for i in args:
		print(i)
	for key,value in kwargs.items():
		print(key,value)	
lis = ('harry','python')
marklist = {'Divyraj':100,'Tony':98,'Peter':95}
master('normal',*lis,**marklist)		