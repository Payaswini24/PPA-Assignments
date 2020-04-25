import re

while True:
	inp=input("enter the name.Type stop when done\n")
	if (inp)=="stop":
		break
	else: 
		name=[]
		string=" "
		for char in inp:
			if char.isalpha():
				name.append(char)
		temp=''.join(name)
		final=re.findall('[A-Z][a-z]*',temp)
		result=string.join(final)
		print(result)

