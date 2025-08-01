# Write a program to create a list of tuples, where each tuple contains an index and the corresponding value from the original list.
mylist = ["a", "b", "c", "d", "e", "f"]
new_list = [(index, value) for index, value in enumerate(mylist)]
print(new_list)
