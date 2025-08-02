# Write a program to count the occurrences of a specific character in a string.
string = "Riya bought an apple and visited a museum in Delhi."

count = 0
for char in string:
    if char.lower() == "a":
        count += 1

print("Number of occurrences of 'a':", count)
