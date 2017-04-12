import re
def correct(text):
	text=re.sub(' +',' ',text)
	c=1
	result=''
	for i in text:
		result+=i + (' ' if i=='.' and re.match('[a-zA-Z]',text[c]) else '')
		c+=1
	return result
print(correct('This   is  very funny  and    cool.Indeed!'))