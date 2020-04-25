import numpy as np
l=int(input("enter the l value "))
m=int(input("enter the number of rows "))
n=int(input("enter the number of col "))

matrix=[[["*"for col in range(n)]
				for row in range(m)]
					for repeat in range(l)]
print(matrix)
