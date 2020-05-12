"""Takes user input for up,down,left and right.
Computes the final x axis and y axis value by (up-down) and (left-right).
Finds the hypothesis value which is the distance travelled """

import math

up_value=int(input("Enter the distance moved upwards "))
down_value=int(input("Enter the distance moved down "))
left_value=int(input("Enter the distance moved left "))
right_value=int(input("Enter the distance moved right "))
y_axis_value=up_value-down_value
x_axis_value=left_value-right_value

distance=math.hypot(y_axis_value,x_axis_value)
print((f"The distance is: {int(distance)}"))
