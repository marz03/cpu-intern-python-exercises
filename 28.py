from  functools import  reduce
def find_longest_word(words):
	return  len(reduce(lambda x,y:x  if len(x)>len(y) else y,words))

words=['aha','dogo','9gag','javascript']
print(find_longest_word(words))