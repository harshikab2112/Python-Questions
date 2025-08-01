# Write a program to remove all occurrences of an element from a list.
my_list = [1, 2, 3, 9, 8, 4, 5, 1, 2, 5, 4]
no_to_remove = 2

new_list = [x for x in my_list if x != no_to_remove]
print(new_list)
# while no_to_remove in my_list:
#     my_list.remove(no_to_remove)
# print(my_list)
