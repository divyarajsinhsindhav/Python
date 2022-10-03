#Method which we can`t use in Tuple like,
#append,pop,insert,remove

#Method which we can use in Tuple 
#count,indexing,len,function,Slicing

i = ("Gujrat","Punjab","Goa","Gujrat","Asam","Maharastra","Keral")

#1.count
print(i.count("Gujrat")) #2 time "Gujrat" in i Tuple

#2.indexing
print(i[:4]) #print Tuple i still postion 3

#3.len
print(len(i)) #print len if i Tuple

#4.function
#5.slicing 
print(i[0:6:2]) #i/p = [1,2,3,4,5,6] #o/p = [1,3,5] 