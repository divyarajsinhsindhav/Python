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


tony = Employee('Tony','Stark',44000)
peter = Employee('Peter','Parker',44000)

print(Employee.no_of_employee)

tony.increase()
print(tony.salary)

#print(Employee.__dict__)
#print(tony.fname , peter.lname)

