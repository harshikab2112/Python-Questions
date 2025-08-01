# Write a program to create a new list that contains only the even numbers from an existing list.
my_list = [1, 2, 4, 5, 6, 7, 3, 2]

new_list = [x for x in my_list if x % 2 == 0]
print(new_list)
