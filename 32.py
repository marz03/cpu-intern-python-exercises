import re
def recognise_palindrome():
	try:
		with open(input('Enter file name:')) as fp:
			lines=fp.read().split('\n')
			for foo in lines:
				line=foo
				line=''.join([i for i in line if re.match('[a-zA-Z]',i)]).lower()
				if line==line[::-1]:
					print(foo)
	except FileNotFoundError:
		print("File Not Found")
	
recognise_palindrome()