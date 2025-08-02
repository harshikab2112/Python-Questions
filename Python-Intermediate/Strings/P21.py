# Write a program to check if two strings are anagrams (contain the same characters in any order).
string1 = input("Enter the first word: ").lower().replace(" ", "")
string2 = input("Enter the second word: ").lower().replace(" ", "")

if len(string1) == len(string2):
    if sorted(string1) == sorted(string2):
        print("Yes, the strings are anagrams.")
    else:
        print("No, the strings are not anagrams.")
else:
    print("No, the strings are not anagrams.")
