def is_palindrome(str):
	ind=len(str)
	for i in str:
		ind=ind-1
		if i != str[ind]:
			return False
	return True

print(is_palindrome('radar'))