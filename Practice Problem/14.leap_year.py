#find leap year or not a leap year using python
#here we use if_else statment

while True:
	year = int(input("Enter year :- "))

	if year%4==0 and year%4!=0 or year%4==0 and year%100==0 and year%400==0:
		print(f"Year {year} is leap year")
		break

	else:
		print(f"Year {year} The is not a leap year")	 
		continue
