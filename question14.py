table_size = input("entern the matrix number \n")
multiplication_table = [[0] * table_size for _ in range(table_size)]
for i in range(1, table_size+1):
    for j in range(1, table_size+1):
        multiplication_table[i - 1][j - 1] = i * j

# Print the multiplication table
for row in multiplication_table:
    for element in row:
        print(element, end='\t')
    print()
