#in keyword
s = {1,2,3,4,5,6}

if 5 in s:
	print("Present")
else:
	print("not Present")

#loop
for i in s:
	print(i)


x = {1,2,3,4,6,8,7,3,4}
y = {4,7,8,3,6,9,5}
#-----------------------------------------
#union
union_set = x | y
print(union_set)

#intersector
intersector_set = x & y
print(intersector_set)	

