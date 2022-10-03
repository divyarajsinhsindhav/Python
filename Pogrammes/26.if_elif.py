age = int(input("Enter your age:- "))

if age == 0 or age < 0:
	print("You enter your wrong age")
elif 0<age<=5:
	print("Ticket Price:Free")	
elif 5<age<=15:
	print("Ticket Price:100")
elif 15<age<=50:
	print("Ticket Price:200")
elif 50<age<=90:
	print("Tiickeet Price:300")
else:
	print("You can't buy Ticket")
