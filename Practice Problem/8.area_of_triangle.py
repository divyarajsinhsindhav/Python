#find area of triangle using ython
#A = [s*{ (s-x) * (s-y) * (s-z) }]**0.5
#s = (x+y+z)/2
#using "Haron's equation"

x = int(input("Enter side x :- "))
y = int(input("Enter side y :- "))
z = int(input("Enter side z :- "))

s = (x+y+z)/2

p = s-x
q = s-y
r = s-z

print(f"Area of Triangle is {(s*(p*q*r))**0.5}")
