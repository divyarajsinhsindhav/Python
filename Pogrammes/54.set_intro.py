#unordered collection of unique items

#remove duplicate value
a = [1,3,6,7,8,9,9,4,8,5,2,4,8,9,6,5,1,3,5,3,8,7]

b = set(a)
print(b)

#add item
x = {1,2,3}
x.add(4)
print(x)

#remove item
i = {7,5,3,4,5,6}
i.remove(5)
print(i)

i.discard(10) #remove item from set without any error 
print(i)	  #if item is not avileble in set we don`t see any type of error

#copy
c = [73,65,4,54,6,87]
p = c.copy()
print(p)
