import re
while True:
	string=input("\nEnter the string.Type'end'when done\n")
	if (string)=="end":
		break
	else: 
		split = re.findall('[A-Z][a-z]*[0-9]*[!@#$&()\\-' ':.+,/\"]*',string)
		result=' '.join(split)
		print(result)

