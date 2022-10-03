#insert & extend method in list
#join two list
name = ["Tobby","Tom"]
print(name)

name.insert(1,"Andrew") #insert Andrew at 1st position
print(name)

n1 = ["Hawkay","Black Widow","Hulk"]
n2 = ["Iron-Man","Captain America","Thor"]
#n = n1 + n2 #List is also join with the help of '+' sign 
n1.extend(n2)
print(n1)

i = ["Dr.Strange","Spider-man","Ant-man","Black Panthor","GOG"]
j = ["Hawkay","Black Widow","Hulk","Iron-Man","Captain America","Thor"]
j.append(i) #Using append method we can also join two list
print(j) #Output with append method :- [1,2,[1,3]]

print(j[6])


