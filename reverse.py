mydict={"hello" : "world", "speckbit" : "self-learning", "life" : "meaning"}
print(mydict)
inp=input("\nenter the value for which you want to find the key\n")
for key,value in mydict.items():
	if value==inp:
			print("The key is :" )
			print((key))
	