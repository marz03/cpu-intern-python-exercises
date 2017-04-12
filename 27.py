#1 Using a for-loop
def map_list1(words):
	list=[]
	for i in words:
		list+=[len(i)]
	return  list
def map_list2(words):
	return list(map(lambda x:len(x),words))
def map_list3(words):
	return [len(i) for  i in words]

words=['dog','cat','animal','me','dragon']
print(map_list1(words))
print(map_list2(words))
print(map_list3(words))