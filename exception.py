numerator=int(input("enter the numerator "))
denominator=int(input("enter the denominator "))


try:
	result= (numerator/denominator)
	print(result)
except ZeroDivisionError as error:
	print("Division by zero!")
