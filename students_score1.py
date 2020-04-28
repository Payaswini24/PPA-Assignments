mydict={}

subject=["Math","Physics","Chemistry","Biolog","Social-Science"]

while True:
	inp=input("enter the student's name and marks ")

	if inp=="":
		break
	inp=inp.split()
	a,b=inp[0],inp[1:]
	mydict[a]=list(map(int,b))


name,sub=input("enter Name & Subject ").split()
i=subject.index(sub)
print(f"{name} scored {mydict[name][i]} in {sub}" )
