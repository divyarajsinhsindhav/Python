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


tony = Employee('Tony','Stark',44000)
peter = Employee('Peter','Parker',74000)

print(tony.salary)
Employee.change_increment(3)
tony.increase()
print(tony.salary)

#print(Employee.__dict__)
#print(tony.fname , peter.lname)
