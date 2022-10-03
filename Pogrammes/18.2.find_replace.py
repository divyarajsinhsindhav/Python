#find
sentence = "talk me cheap show me the code"
print(sentence.find("me"))
sentence = "your future is created by what you do today not tommorow"
print(sentence.find("is"))
sentence = "We are good students"
print(sentence.find("good"))
sentence = "He is good student and He is good writer"
print(sentence.find("is"))
sentence = "He is good student and He is good writer"
print(sentence.find("is",5)) #find "is" from 5th position

#if we don't know first "is" position & we want find second "is" position
sentence = "He is good student and He is good writer"
first_pos = sentence.find("is")
second_pos = sentence.find("is",first_pos +1)
print(second_pos)