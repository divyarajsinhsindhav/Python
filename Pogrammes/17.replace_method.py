#Clear unwanted space from the middel of the user input
name = input("Please enter your name:- ")
dots = "........."

print(name.replace(" ",""))

print(name.strip().replace(" ","") + dots) #Strip method + Replace method
