def find_longest_word(words):
	longest=0
	for word  in words:
		if len(word)>longest:
			longest=len(word)
	return longest

words=['dog','bath','amazing','hello','python']
print(find_longest_word(words))