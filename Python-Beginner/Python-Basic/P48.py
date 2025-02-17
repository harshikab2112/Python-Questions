# Accept an input number and check if it is a palindrome (e.g., 121 is a palindrome).

num = input("Enter a number: ")

if num == num[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
