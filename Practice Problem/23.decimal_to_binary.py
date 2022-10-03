#covert decimal number in number
#decimal number is 10
#LOGIC: 10%2=1
#		5%2=0
#		2%2=1		
#Than binary number :- 1010

def convert(i):
	if i>1:
		convert(i//2)
	print(i%2,end='')

n = int(input("Enter decimal number :- "))
convert(n)
print()		