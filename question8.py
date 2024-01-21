# Create a program that uses a loop to print the multiplication table of a given number.
number = int(input("enter the number :\n"))
i = 1
for i in range(1, 11):
    mul_num = number * i
    print(f"{number} * {i} = {mul_num}")
