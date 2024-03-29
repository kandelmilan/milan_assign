"""
 Write a Python program to print the Fibonacci 
 sequence up to a certain number using a loop. 

 """


max_number = int(input("Enter the maximum number in the Fibonacci sequence: "))
fibonacci_sequence = [0, 1]

while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= max_number:
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)


print("Fibonacci sequence up to", max_number, ":", fibonacci_sequence)
