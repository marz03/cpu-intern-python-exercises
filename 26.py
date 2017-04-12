from functools import reduce
def  max_in_list(list):
	return reduce(lambda x,y: x if x>y else y,list)

print(max_in_list([1,2,5,3,4]))