class Employee:

	increment = 1.5
	no_of_employee = 0
	def __init__(self,fname,lname,salary): #__init__ called dunder init
		self.fname = fname
		self.lname = lname
		self.salary = salary
		Employee.no_of_employee += 1

	def increase(self):
		self.salary = int(self.salary * self.increment)

	@property	
	def email(self):
		if self.fname == None:
			return 'Email not set'
		else:
			return self.fname + '.' + self.lname + '@pymail.com'	

	@email.setter #We can change email as our wish
	def email(self,given_email):	
		name_list = given_email.split('@')[0].split('.')	
		self.fname = name_list[0]
		self.lname = name_list[1]

	@email.deleter
	def email(self):
		self.fname = None	
		self.lname = None

	@classmethod
	def change_increment(cls,amount):	
		cls.increment = amount

	@classmethod
	def from_str(cls,emp_string):
		fname,lname,salary = emp_string.split('-')	
		return cls(fname,lname,salary)

	@staticmethod
	def isopen(day):
		if day == 'sunday':	
			return False
		else:
			return True

	
	def __add__(self,other):
		return self.salary + other.salary

	def __repr__(self):
		return 'Employee({},{},{})'.format(self.fname,self.lname,self.salary)
					
	def __str__(self):	
		return 'The name of Employee is {}'.format(self.fname)

if __name__ == '__main__':
	tony = Employee('Tony','Stark',44000)
	tom = Employee('Tom','Parker',74000)
	print(tony.email , tom.email)
	tom.lname = 'Holand' #change lname of Tom
	print(tom.email)
	tom.email =  'Tobby.holand@pymail.com'
	print(tom.email) 
	del tom.email
	print(tom.email)
	



'''
bruce = Employee('Bruce','Banner',123000)
tony = Employee('Tony','Stark',44000)
peter = Employee('Peter','Parker',74000)
stephen = Employee('Stephen','Strange',68000)
steve = Employee.from_str('Steve-Rogers-55000')
'''

#print(str(tony))
#print(repr(tony))
#print(tony+peter)
#print(help(Employee))
#print(Employee.__dict__)
#print(tony.fname , peter.lname)
#print(steve.fname)
#print(steve.lname)
#print(steve.salary)
#print(Employee.isopen('monday'))