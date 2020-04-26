def score(name,m1,p1,c1,b1,ss1):
	mydict={"Name":name,"Math":m1,"Physics":p1,"Chemistry":c1,"Biology":b1,"Social-Science":ss1}
	while True:
			inp2=input("enter the name and subject.Type stop to end ")
			if inp2==("stop"):
				break
			else:
				nam,sub=inp2.split()
				for k,v in mydict.items():
					if k==sub:
						print(name,"scored",v,"in",sub)

def myfu(ele):
	x,a,b,c,d,e=ele.split()
	score(x,a,b,c,d,e)

i=6
lst=[]
while(i>2):
	inp1=input("enter NAME AND MARKS\n")
	if inp1=="stop":
		break
	else:
		i=i-1
		lst.append(inp1)
for ele in lst:
	sp=str(lst).strip('[]')
	print(sp)
	x=map(myfu(ele),ele)
#sub=sp.split(' ')
#print(sub)

#res.append(sub)
#print(res)
	
	#final=dict(zip(lst2,ele))
	#print((final))

#for ele in lst:
#	sp=str(lst).strip('[]')
	

#	



