import re

n= int(input("\nenter the number of inputs\n"))
for i in range(0,n):
	string=input("\nEnter the string\n")
	split = re.findall('[A-Z][a-z]*[0-9]*[!@#$&()\\-' ':.+,/\"]*',string)
	result=' '.join(split)
	print(result)
