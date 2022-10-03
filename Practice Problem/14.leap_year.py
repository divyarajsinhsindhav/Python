#find leap year or not a leap year using python
#here we use if_else statment

while True:
	n = int(input("Enter year :- "))

	if n%4==0 and n%4!=0 or n%4==0 and n%100==0 and n%400==0:
		print(f"Year {n} is leap year")
		break

	else:
		print(f"Year {n} is not a leap year")	 
		continue