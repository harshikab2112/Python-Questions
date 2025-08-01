# Write a program to merge two lists into one and remove duplicates.
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list2 = [1, 4, 5, 7, 2, 9]

new_list = my_list1 + my_list2
unique_list = []
for num in new_list:
    if num not in unique_list:
        unique_list.append(num)

print(unique_list)
