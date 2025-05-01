# 26.04.2025


import os

def ft_filter(lst):
	res = []
	for arg in lst:
		while arg and not arg[0].isalnum():
			arg = arg[1:]
		while arg and not arg[-1].isalnum():
			arg = arg[:-1]
		if arg:
			res.append(arg)
	return res

_input = input("Type the path of your file: ")


while True:
	if os.path.exists(_input):
		with open(_input, 'r') as f:
			txt = f.read()
			break
	else:
		print("Error")

print("Number of characters: ", len(txt))
print("Number of characters (without spaces): ", len(txt) - txt.count(' '))
print("Number of words: ", len(txt.split()))
print("Number of sentences: ", txt.count('.') + txt.count('!') + txt.count('?'))
print("Unfiltered word count: ")
lst = ft_filter(map(lambda s: s.lower(), txt.split()))
lst_filer = sorted(set(lst), key=lambda x: lst.count(x), reverse=True)
for word in lst_filer:
	if lst.count(word) == 1:
		break
	else:
		print(word, '\t', lst.count(word))
