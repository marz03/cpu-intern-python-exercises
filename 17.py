def is_my_palindrome(str):
	str=str.lower()
	str=[ch for ch in str if ch in 'abcdefghijklmnopqrstuvwxyz']
	size=len(str)
	for ch in str:
		size=size-1
		if ch!=str[size]:
			return False
	return True

words=["Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", "Dammit, I'm mad!"]
for i in  words:
	print(is_my_palindrome(i))