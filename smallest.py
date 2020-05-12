"""appends the user's input to an empty string. User is expected to type 'end'when done.
The program returns the smallest number from the list of numbers entered by the user"""



list_of_num=[]
print(("enter the numbers.Type 'end' when done.\n"))
	
while True:
		user_input=input()
		if user_input=="end":
			break
		user_input=int(user_input)
		list_of_num.append(user_input)
		list_of_num.sort()
print(list_of_num)
nth_value=int(input("Enter the nth value "))
index=(nth_value-1)
print(f"The expected smallest number is\n{ list_of_num[index]}")