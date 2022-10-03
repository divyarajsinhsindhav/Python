#Wordd count in Dictionary

def word_count(a):
	count_word = {}
	for i in a:
		count_word[i] = a.count(i)
	return count_word

print(word_count("Divyrajsinh"))		
