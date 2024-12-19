a=input("Enter a string with numbers: ")
numericDigit=""

for char in a:
    if char.isdigit():
        numericDigit +=char
print("Numeric characters in the string:", numericDigit)