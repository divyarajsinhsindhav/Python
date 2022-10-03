class Employee:

	increment = 1.5
	no_of_employee = 0
	def __init__(self,fname,lname,salary):
		self.fname = fname
		self.lname = lname
		self.salary = salary
		Employee.no_of_employee += 1

	def increase(self):
		self.salary = int(self.salary * self.increment)

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


class pogrammer(Employee):
	def __init__(self,fname,lname,salary,programming_lang,exp):
		super().__init__(fname,lname,salary)
		self.programming_lang = programming_lang
		self.exp = exp

	def increase(self):
		self.salary = int(self.salary * (self.increment+0.2))
		return self.salary

bruce = pogrammer('Bruce','Banner',123000,'Python',5)
print(bruce.programming_lang)
print(bruce.increase())
		

'''
tony = Employee('Tony','Stark',44000)
peter = Employee('Peter','Parker',74000)
stephen = Employee('Stephen','Strange',68000)
steve = Employee.from_str('Steve-Rogers-55000')
'''

#print(help(pogrammer))
#print(Employee.__dict__)
#print(tony.fname , peter.lname)
#print(steve.fname)
#print(steve.lname)
#print(steve.salary)
#print(Employee.isopen('monday'))