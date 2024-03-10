start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start_range} and {end_range} are:")

# Iterate through each number in the range
for num in range(start_range, end_range + 1):
    # Skip 1 and numbers less than 2
    if num < 2:
        continue
    
    # Check if the current number is prime
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    # Print the prime number
    if is_prime:
        print(num)