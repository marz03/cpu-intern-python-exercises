def generate_n_chars(n,c):
	result=''
	while n!=0:
		result=result+c
		n=n-1
	return result

print(generate_n_chars(5,'x'))