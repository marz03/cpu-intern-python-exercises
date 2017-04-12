import re
def make_ing_form(verb):
	if re.match('[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z][aeiouAEIOU][b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]$',verb[-3:]):
		return verb+verb[-1:]+'ing'
	if verb.endswith('ie'):
		return verb[:-2]+'ying'
	if verb.endswith('e'):
		return verb[:-1]+'ing'
	return  verb+'ing'

print(make_ing_form('lie'))
print(make_ing_form('see'))
print(make_ing_form('move'))
print(make_ing_form('hug'))
print(make_ing_form('debug'))