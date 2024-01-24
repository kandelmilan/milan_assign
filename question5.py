# Write a program to remove duplicate elements from a list.
name_list1 = ["ant", "aeroplane", "apple", "ball", "ant"]

non_duplicates = []
for i in name_list1:
    if i not in non_duplicates:
        non_duplicates.append(i)


print(non_duplicates)
