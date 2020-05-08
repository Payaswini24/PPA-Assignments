n=int(input("enter the numberator "))
d=int(input("enter the denominator "))


try:
	result= (n/d)
	print(result)
except ZeroDivisionError as error:
	print("Division by zero!")