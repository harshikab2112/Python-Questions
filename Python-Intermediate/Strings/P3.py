# Write a program to count the number of vowels in a string.
string = "riya is a good girl"
count = 0
for char in string.lower():
    if char in "aeiou":
        count += 1
print(count)
