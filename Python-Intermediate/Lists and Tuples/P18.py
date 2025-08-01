# Write a program to find the common elements between two lists.
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list2 = [1, 4, 5, 7, 2, 9]

new_list = [x for x in my_list1 if x in my_list2]
print(new_list)
