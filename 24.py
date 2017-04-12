def make_3sg_form(verb):
	if verb.endswith('y'):
		return verb[:-1]+'ies'
	if verb.endswith(('o','ch','s','sh','x','z')):
		return verb+'es'
	return verb +'s'
print(make_3sg_form('try'))
print(make_3sg_form('brush'))
print(make_3sg_form('run'))
print(make_3sg_form('fix'))