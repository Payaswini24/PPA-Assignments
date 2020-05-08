class Parking:
	def __init__(self):
		self.count1= 0
		self.count2=0
		#self.entry=entry
		self.exit= exit
		self.rem2=100
		self.rem=100
	
		
	def menu(self):
		while True:	
			print("---------------------------")
			ch=int(input("1) For 2-Wheeler\n2) For 4-wheeler\n3) To End\n"))
			if ch==1: 
				inp=int(input("for 2-wheeler: Press 1 for entry and 2 for exit\n"))
				if inp== 1:
					self.entry=int(input("enter the number of 2 wheeler entered "))
					#self.count1+= self.entry
					self.rem = self.rem-self.entry
					print(f"Available slots for 2-Wheeler:{self.rem}")
				elif inp==2: 
					self.exit=int(input("enter the number of 2 wheeler exited "))
					self.rem+=self.exit
					print(f"Available slots for 2-Wheeler:{self.rem}")
				else:
					print("Enter Valid option")
				

			elif ch==2:	
				inp=int(input("4 wheeler: Press 1 for entry and 2 for exit\n"))
				if inp== 1:
					self.entry=int(input("enter the number of 4 wheeler entered "))
					#self.count2+= self.entry
					self.rem2 = self.rem2-self.entry
					print(f"Available slots for 4-Wheeler:{self.rem2}")
				elif inp==2: 
					self.exit=int(input("enter the number of 4 wheeler exited "))
					self.rem2+=self.exit
					print(f"Available slots for 4-Wheeler:{self.rem2}")
				else:
					print("Enter Valid option")
				
			if ch==3:
				break


p1=Parking()
p1.menu()

#p2=Parking()
#p1.four_wheeler_enter()