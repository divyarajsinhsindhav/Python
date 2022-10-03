class Employee:
	def __init__(self,fname,lname,salary):
		self.fname = fname
		self.lname = lname
		self.salary = salary

tony = Employee('Tony','Stark',44000)
peter = Employee('Peter','Parker',44000)

print(tony.fname , peter.lname)


