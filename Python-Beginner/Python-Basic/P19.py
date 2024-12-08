num0=float(input("Enter the decimal number: "))

"""Since we can't convert floator decimal directly
into these. Now we will convert float into int first.
Then convert them into these forms."""
num=int(num0)

print("Binary value:", bin(num))
print("Octal value:", oct(num))
print("Hexadecimal value:", hex(num))