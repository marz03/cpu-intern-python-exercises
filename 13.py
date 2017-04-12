def max_in_list(list):
	max=list[0]
	for i in list:
		if i>max:
			max=i
	return max

print(max_in_list([12,34,75,33,0,23]))