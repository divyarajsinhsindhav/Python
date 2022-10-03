#Count
#Sort Method
#Sorted Method
#Reverse
#Clear
#Copy

name = ["Robert","Tom","Chris","Bendict","Mark","Chris"]
print(name.count("Chris")) #How many times "Chris" word in List? 

name = ["Dhoni","Virat","Jadeja","Ashwin","Hardik Pandya","Bumrah"]
name.sort() #All elements are sort as ABCD....... 
print(name) #Orignal List change 

name = ["Iron-Man","Captain America","Thor","Spider-Man","DR.Strange","Hulk"]
print(sorted(name)) #Shorted method change only List not Orignel list
#print(name)		#Outpt :- Orignal List print

name = ["Roman Reigns","Seth Rollins","Rock","Steve Austine","Edge"]
name.reverse() #List written in Reverse
print(name)

name = ["Ronaldo","Messi","Naymar"]
name.clear() #clear list
print(name)

name = ["Google","Apple","Microsoft","Samsung","IBM"]
name1=name.copy() #name list copy in name1 list
print(name1)

n = [9,7,8,5,6,3,4,1,2,0]
n.sort()
print(n)


