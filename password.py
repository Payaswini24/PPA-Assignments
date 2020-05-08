lst=['$','#','@']
inp=input("Enter the password\n")

if (len(inp)<8):
	print("invalid ")

if (len(inp)>16):
	print("invalid")

elif not any(char.isdigit() for char in inp):
	print("invalid")

elif not any(char.isupper() for char in inp):
	print("invalid")

elif not any(char.islower() for char in inp):
	print("invalid")

elif not any(char in lst for char in inp):

	print("invalid")

else:
	print("Valid")