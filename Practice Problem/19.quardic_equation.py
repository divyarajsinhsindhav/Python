#Quardic Equation
#ax**2 + bx + c = 0

a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))

d= (b**2)-(4*a*c)

print("d is" ,d)

x1= (-b+(d**0.5))/2*a
x2= (-b-(d**0.5))/2*a


if d>=0:
	print("Equation is possible")
	print(f"x is {x1} \nor \nx is {x2}")

else:
	print("Equation is not possible")

