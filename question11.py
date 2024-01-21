string = input("Enter any string : ")
count = 0
lwr_string = string.lower()
for i in lwr_string:
    if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        count = count+1
print(f"There contain {count} vowels in the string")
