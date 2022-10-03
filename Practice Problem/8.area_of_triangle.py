#find area of triangle using ython
#A = [s*{ (s-a) * (s-b) * (s-c) }]**0.5
#s = (a+b+c)/2
#using "Haron's equation"

a = int(input("Enter side a :- "))
b = int(input("Enter side b :- "))
c = int(input("Enter side c :- "))

s = (a+b+c)/2

p = s-a
q = s-b 
r = s-c

print(f"Area of Triangle is {(s*(p*q*r))**0.5}")