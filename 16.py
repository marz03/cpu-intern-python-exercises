def filter_long_words(words,n):
	return [i for i in words if len(i)>n]

words=['dog','bath','amazing','hello','python']
print(filter_long_words(words,5))