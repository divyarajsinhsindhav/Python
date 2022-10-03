#To delete in list we can use del,pop,remove
n = [1,2,4,5,6,7,8,9]
print(n)
n.remove(1)
print(n)

i = ["php","Python","C++"]
print(i)
i.pop() #last element is delete when we use .pop
print(i)

j = [1,2,3,4,5,6,7,8,9]
print(j)
j.pop(2) #'2' is show the position in list #2nd position element is deleted from the list 
print(j)

k = ["Samsung","Apple","Google","OnePluse","Huwai"]
print(k)
del k[4] #'del' oprater is delete 4th position element  
print(k)

x = ["Django","Laravel","node.js","React.js","NEXT.js"]
print(x)
pop_item = x.pop(2) #pop is also use for find something from list
print(pop_item)