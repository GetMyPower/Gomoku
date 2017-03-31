import re
pattern = 'X+'
txt = '@@X  X@X  XXXX@  X'
for i in re.finditer(pattern, txt):
	print(i.span()[0])
