class Todo: 
	def __init__(self):

		self.lst=[]

		self.lst2=[]
		

	def add(self):
		while True:
			self.ch=int(input("1)To add task\n2)when done adding\n"))
			if (self.ch==1): 	
				inp=input("enter the task to be done\n")
				self.lst.append(inp)
				print(self.lst)
			else:
				break
				

	def mark_done(self):
		while True:	
			self.ch=int(input("1)To mark as done\n2)To exit\n"))
			if self.ch==1:
				inp2=input("enter the job completed\n")
				if inp2 in self.lst:
					self.lst.remove(inp2)
				self.lst2.append(inp2)
				#print(self.lst2)
			else:
				break

	def display(self): 
		print(f"The to do list contains {self.lst}")
		print(f"The tasks completed are {self.lst2}")





p=Todo()
p.add()
p.mark_done()
p.display()
