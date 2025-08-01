# Write a program to flatten a nested list (convert it to a single list).
my_list = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]

new_list = [num for sub_list in my_list for num in sub_list]
print("Original list:", my_list)
print("Flatten list:", new_list)
