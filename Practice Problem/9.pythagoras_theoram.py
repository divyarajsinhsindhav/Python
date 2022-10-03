#pythagoras theoram using python
#ΔABC is perpandicular
#side AB = perpandicular
#     BC = base
#	  AC = hypotenuse
#AC**2 = AB**2 + BC**2

print("Enter side AB & BC for find hypotenuse lenth")

a = int(input("Enter side AB :- "))
b = int(input("Enter side BC :- "))	 

ab = a**2
bc = b**2

print(f"Hypotenuse of triangle is {(ab + bc)**0.5}")