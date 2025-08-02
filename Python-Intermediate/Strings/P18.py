# Write a program to replace all vowels in a string with a specific character.
string = "Riya bought an apple and visited a museum in Delhi."
new_string = ""

for char in string:
    if char.lower() in "aeiou":
        new_string += "*"
    else:
        new_string += char

print(new_string)
