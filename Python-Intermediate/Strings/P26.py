# Write a program to remove punctuation from a string.
punctuation_marks = [
    ".",
    ",",
    "?",
    "!",
    ":",
    ";",
    "'",
    '"',
    "(",
    ")",
    "- ",
    "...",
    "/",
    "\\",
    "@",
    "#",
    "*",
    "&",
    "%",
    "^",
    "_",
    "~",
]

string = "Riya bought an apple, visited a museum - and said: “Wow! It's beautiful.”"

clean_text = ""
for char in string:
    if char not in punctuation_marks:
        clean_text += char

print(f"Before:\n{string}")
print(f"After\n{clean_text}")
