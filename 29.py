def filter_long_words(words,n):
	return list(filter(lambda x:len(x)>n,words))
words=['javascript','java','c','python']
print(filter_long_words(words,5))