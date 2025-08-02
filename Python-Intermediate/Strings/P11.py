# Write a program to check if a string is a palindrome (reads the same forward and backward).
string = "AbCdEdcba"
print(string.lower() == string[::-1].lower())
