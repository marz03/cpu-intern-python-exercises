def char_freq(str):
	letters={}
	for i in str:
		if i in letters:
			letters[i]+=1
		else:
			letters[i]=0
	return letters

print(char_freq("abbabcbdbabdbdbabababcbcbab"))