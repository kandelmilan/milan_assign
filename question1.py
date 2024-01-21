# Write a Python program to calculate the area and circumference of a circle with a given radius from terminal.
pi = 3.14
radius = int(input("enter the radius of the circle:\n"))
area = radius*radius*pi
print(f"the area of circle with radius {radius} is {area}")
circumference = 2*radius*pi
print(f"the circumference of circle with radius {radius} is {circumference}")
