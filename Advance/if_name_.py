import os

def addition_of_numbers(i,j):
	return i+j

n1 = int(input("Enter number 1 :- "))
n2 = int(input("Enter number 2 :- "))

print(addition_of_numbers(n1,n2))

print(__name__)

def main():
	print(os.listdir("/"))
	print('Hello Django')
print(main())	

if __name__ == '__main__':
	main()