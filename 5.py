def translate(str):
	translated=''
	for  ch in str:
		translated =translated + ((ch+'o'+ch) if ch.lower() in 'bcdfghjklmnopqrstvwxyz' else ch)
	return translated

print(translate('this is fun'))