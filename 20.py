def translate(eng_words):
	dict={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
	return [dict[i] for i in eng_words]

eng_words=['merry','christmas','and','happy','new','year']
print(translate(eng_words))