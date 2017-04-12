def overlapping(a,b):
	for m in a:
		for n in b:
			if m==n:
				return True
	return False

x=[1,2,3,4]
y=[0,5,6,7,8]
print(overlapping(x,y))