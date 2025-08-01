# Write a program to get the unique elements from a list (remove duplicates).
my_list = [1, 2, 3, 9, 8, 4, 5, 1, 2, 5, 4]

new_list = []
for num in my_list:
    if num not in new_list:
        new_list.append(num)

print(new_list)
