def sum(list):
	ans=0
	for i in list:
		ans=ans+i
	return ans

def multiply(list):
	ans=1
	for i in list:
		ans=ans*i
	return ans
	

print(sum([1,2,3,4]))
print(multiply([1,2,3,4]))