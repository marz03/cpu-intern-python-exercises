def reverse(str):
	index=len(str)
	reversed=""
	while index>0:
		index=index-1
		reversed=reversed+str[index]
	return reversed

print(reverse('I am testing'))