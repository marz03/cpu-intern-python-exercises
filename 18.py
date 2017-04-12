def is_pangram(str):
	alphabet='abcdefghijklmnopqrstuvwxyz'
	letters={key:0 for key in alphabet}
	for i in str:
		if i in alphabet:
			letters[i]=letters[i]+1
	return 0 not in letters.values()

print(is_pangram("The quick brown fox jumps over the lazy dog"))