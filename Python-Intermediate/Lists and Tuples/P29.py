# Write a program to rotate a list by N positions to the left.
my_list = [1, 2, 3, 4, 5, 6, 7]
n = int(input("Enter how many times to rotate the list to left: "))

n = n % len(my_list)
rotated_list = my_list[n:] + my_list[:n]
print(f"Rotated list is: ", rotated_list)
