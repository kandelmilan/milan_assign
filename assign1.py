
# Write a Python program to calculate the area and circumference of a circle with a given radius from terminal.
pi = 3.14
radius = int(input("enter the radius of the circle:\n"))
area = radius*radius*pi
print(f"the area of circle with radius {radius} is {area}")
circumference = 2*radius*pi
print(f"the circumference of circle with radius {radius} is {circumference}")
breakpoint()

"""
 Write a Python program that acts as a simple arithmetic calculator. The program should prompt the user to enter two numbers and an arithmetic operation (addition, subtraction, multiplication, or division). 
Based on the user's input, the program should perform the corresponding operation and display the result. Ensure proper handling of division by zero.
"""
num1 = int(input("enter the  first number :\n"))
num2 = int(input("enter the second number:\n"))

arth_opr = input(
    "which  arithmetic operation  you want to perform:\naddition\nsubtraction\nmultiplication\ndivision\n")

if arth_opr == "addition":
    output = num1+num2
    print(output)
elif arth_opr == "subtraction":
    output = num1-num2
    print(output)
elif arth_opr == "multiplication":
    output = num1*num2
    print(output)
elif arth_opr == "division" and num2 != 0:
    output = num1/num2
    print(output)
else:
    print("not available")


breakpoint()
# Create a list of integers and then write a Python program to find the sum of all the elements in the list.
number_list = [1, 2, 3, 4, 5, 6, 7, 8]
sum = sum(number_list)
print(sum)
breakpoint()

# WAP to demonstrate the use case of insert() and extend() methods in Python lists.
name_list = ["ram", "shyam", "hari", "geeta", "sita"]
name_list.insert(5, "rajan")
name_list.extend("rajan")
print(name_list)
breakpoint()

# Write a program to remove duplicate elements from a list.
name_list1 = ["ant", "aeroplane", "apple", "ball"]
name_list1.remove("ball")
print(name_list1)

breakpoint()

# Reverse a given string without using the reverse function or slicing.
friut_name = "apple"

print(friut_name[::-1])

breakpoint()

# Write a Python program to check if a given string is a palindrome.
number = input("enter the number :\n")
if number == number[::-1]:
    print("number is palindormi")
else:
    print("number is palindormi")

breakpoint()

# Create a program that uses a loop to print the multiplication table of a given number.
number = int(input("enter the number :\n"))
i = 1
for i in range(1, 11):
    mul_num = number * i
    print(f"{number} * {i} = {mul_num}")

breakpoint()

# Explain the difference between the find() and index() methods for strings.


list = ["bmw", "toyota", "suzuki", "lambo", "tata"]

index_element = list[4]
print(index_element)


list_n = "hello !!!"
find_element = list_n.find("ll")
print(find_element)
breakpoint()

"""
# Write a Python program to print the Fibonacci sequence up to a certain number using a loop.
num_list = [0, 1]
i=1
for i in range(1,11):
        sum = num_list[0]+num_list[1]
# not completed
"""
