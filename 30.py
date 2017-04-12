def  translate(words):
	return list(map(lambda x:{"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}[x],words))

eng_words=['merry','christmas','and','happy','new','year']
print(translate(eng_words))