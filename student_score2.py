mydict={'Alex': [50, 98, 69, 78, 89], 'Steve': [78, 87, 98, 88, 79], 
		'Martin': [45, 99, 100, 89, 88], 'Trish': [66, 68, 70, 71, 68]}
lst=[]

subject=["Math","Physics","Chemistry","Biology","Social-Science"]

sub=input("enter the subject ")
i=subject.index(sub)
lst=[(k,v[i])for k,v in mydict.items()]
#print(lst)
tup=sorted(lst, key = lambda x: x[1],reverse=True) 
print(tup)
