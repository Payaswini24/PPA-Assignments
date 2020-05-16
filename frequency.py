lst=[]

inp=input("enter the string\n")

inp=list(inp.split(" "))
inp.sort()

for i in inp:
	if i not in lst:
		lst.append(i)

for i in range(0,len(lst)):
	print(f"{lst[i]}: {inp.count(lst[i])}")
