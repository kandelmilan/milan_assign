"""
 Write a Python program that acts as a simple arithmetic calculator. The program should prompt the user to enter two numbers and an arithmetic operation (addition, subtraction, multiplication, or division). 
Based on the user's input, the program should perform the corresponding operation and display the result. Ensure proper handling of division by zero.
"""
num1 = int(input("enter the  first number :\n"))
num2 = int(input("enter the second number:\n"))

arth_opr = input(
    "which  arithmetic operation  you want to perform:\naddition\nsubtraction\nmultiplication\ndivision\n")

if arth_opr == "+":
    output = num1+num2
    print(output)
elif arth_opr == "-":
    output = num1-num2
    print(output)
elif arth_opr == "*":
    output = num1*num2
    print(output)
elif arth_opr == "/" and num2 != 0:
    output = num1/num2
    print(output)
else:
    print("not available")
