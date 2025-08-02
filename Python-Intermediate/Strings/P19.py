# Write a program to find all words in a string that start with a specific letter.
string = "Riya bought an apple and visited a museum in Delhi."
words = string.replace(".", "").replace(",", "").split()

mylist = [word for word in words if word.lower().startswith("a")]
print(mylist)
