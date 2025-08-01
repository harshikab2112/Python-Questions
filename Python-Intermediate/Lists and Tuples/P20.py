# Write a program to sum the elements of a list of lists (nested list).
my_list = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
total = 0

for sub_list in my_list:
    for num in sub_list:
        total += num

print("Sum of elements of list of lists is", total)

# total_sum = sum([num for sub_list in my_list for num in sub_list])
# print("Sum of elements of list of lists is", total_sum)
