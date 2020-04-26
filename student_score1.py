

def score(name,m1,p1,c1,b1,ss1):
	mydict={"Name":name,"Math":m1,"Physics":p1,"Chemistry":c1,"Biology":b1,"Social-Science":ss1}
	nam,sub=input("Enter Name and Subject ").split()
	for k,v in mydict.items():
		if k==sub:
			print(name,"scored",v,"in",sub)



n=int(input("Enter the total number of students "))
for i in range(0,n):
	x,a,b,c,d,e=(input("Enter the Name and Marks\n")).split()
	score(x,a,b,c,d,e)
	


