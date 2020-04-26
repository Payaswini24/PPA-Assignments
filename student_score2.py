print("Alex 78 78 67 56 89\nSteve 54 67 89 87 65\nTrish 56 78 87 89 90\nMartin 48 89 85 82 81")
inp1=input("choose a subject\n")

mydict={"Name":["Alex","Steve,Trish,Martin"],"Math":[78,54,56,48],"Physics":[78,67,78,89],"Chemistry":[67,89,87,85],
		"Biology":[56,87,89,82],"Social-Science":[89,65,90,81]}
for k,v in mydict.items():
	if k==inp1:
		j=(str(mydict["Name"])).strip('[]')
		print(j)
		mrks=(str(v)).strip('[]')
		print(mrks)